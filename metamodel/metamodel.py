import metamodel.grammar as gr
import metamodel.fuzzy as fz
from copy import copy

class Expression:
    # def __init__(self, parent, concrete):
    #     self.parent = parent
    #     self.concrete = concrete
    #     if (concrete != None):
    #         self.root = concrete.abstract_syntax()
    pass

class Addition(Expression):
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return "Addition({},{})".format(str(self.l),str(self.r))
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return self.l.eval() + self.r.eval()
    def assign(self, varstate):
        return Addition(self.l.assign(varstate), self.r.assign(varstate))
        
class Subtraction(Expression):
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return "Subtraction({},{})".format(str(self.l),str(self.r))
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return self.l.eval() - self.r.eval()
    def assign(self, varstate):
        self.l.assign(varstate)
        self.r.assign(varstate)
        return Subtraction(self.l.assign(varstate), self.r.assign(varstate))

        
class Multiplication(Expression):
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return "Multiplication({},{})".format(str(self.l),str(self.r))
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return self.l.eval() * self.r.eval()
    def assign(self, varstate):
        self.l.assign(varstate)
        self.r.assign(varstate)
        return Multiplication(self.l.assign(varstate), self.r.assign(varstate))
        
        
class Division(Expression):
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return "Division({},{})".format(str(self.l),str(self.r))
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return self.l.eval() / self.r.eval()
    def assign(self, varstate):
        self.l.assign(varstate)
        self.r.assign(varstate)
        return Division(self.l.assign(varstate), self.r.assign(varstate))
        
class Term:
    pass

class Var(Term):
    def __init__(self, var, indexlist=[]):
        self.var = var
        self.indexlist = indexlist
        self.value = None
    def __str__(self):
        if self.indexlist == []:
            return str(self.var)
        else:
            return str(self.var) + '[' + ', '.join([str(i) for i in self.indexlist])  + ']'
    def FV(self):
        if self.value == None:
            return {self}
        else:
            return set()
    def __hash__(self):
        return hash((self.var,tuple(self.indexlist)))
    def __eq__(self, other):
        return self.var == other.var and self.indexlist == other.indexlist
    def eval(self):
        assert self.value != None
        return self.value
    def assign(self, varstate):
        ret = copy(self)
        if self in varstate:
            ret.value = varstate[self]
        return ret

class Val(Term):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)
    def FV(self):
        return set()
    def eval(self):
        return self.val
    def assign(self, varstate):
        return copy(self)
        
class VariableTransform:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
    def FV(self):
        return self.expr.FV()
    def assign(self, varstate):
        return VariableTransform(self.var, self.expr.assign(varstate))

    
class VariableTransforms:
    def __init__(self, v=None):
        if v==None:
            self.v = []
        else:
            self.v = v
    def FV(self):
        return set().union(*[e.FV() for e in self.v])
    def assign(self, varstate):
        return VariableTransforms([it.assign(varstate) for it in self.v])
    def apply(self, varstate):
        ret = copy(varstate)
        for vt in self.v:
            ret[Var(vt.var)] = vt.assign(varstate).expr.eval()
        return ret
    
class Constraint:
    pass

class TrueConstraint(Constraint):
    def __init__(self):
        pass
    def FV(self):
        return set()
    def eval(self):
        return 1
    def assign(self, varstate):
        return copy(self)

class BinRel(Constraint):
    pass

class LeqRel(BinRel):
    def __init__(self, l, r, delta):
        self.l = l
        self.r = r
        self.delta = delta
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return fz.fuzzyleq(self.r.eval(), self.delta)(self.l.eval())
    def assign(self, varstate):
       return LeqRel( self.l.assign(varstate),
                      self.r.assign(varstate),
                      self.delta)
    
class GeqRel(BinRel):
    def __init__(self, l, r, delta):
        self.l = l
        self.r = r
        self.delta = delta
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return fz.fuzzygeq(self.r.eval(), self.delta)(self.l.eval())
    def assign(self, varstate):
       return GeqRel( self.l.assign(varstate),
                      self.r.assign(varstate),
                      self.delta)

    
class EqRel(BinRel):
    def __init__(self, l, r, delta):
        self.l = l
        self.r = r
        self.delta = delta
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return fz.fuzzyeq(self.l.eval(), self.r.eval(), self.delta)
    def assign(self, varstate):
       return EqRel( self.l.assign(varstate),
                     self.r.assign(varstate),
                     self.delta)

    
class TerRel(Constraint):
    pass

class IntervalRel(TerRel):
    def __init__(self, first, second, third, delta):
        self.first = first
        self.second = second
        self.third = third
        self.delta = delta
    def FV(self):
        return set.union(self.first.FV(), self.second.FV(), self.third.FV())
    def eval(self):
        return fz.fuzzyinterval(self.third.eval(), self.first.eval(), self.delta)(self.second.eval())
    def assign(self, varstate):
       return IntervalRel( self.first.assign(varstate),
                           self.second.assign(varstate),
                           self.third.assign(varstate),
                           self.delta)


class Conjunction(Constraint):
    def __init__(self, l, tnorm, r):
        self.l = l
        self.tnorm = tnorm
        self.r = r
    def FV(self):
        return set.union(self.l.FV(), self.r.FV())
    def eval(self):
        return self.tnorm.compute(self.l.eval(), self.r.eval())
    def assign(self, varstate):
        return Conjunction( self.l.assign(varstate),
                            self.tnorm,
                            self.r.assign(varstate))
        
class Tnorm:
    def compute(a, b):
        pass

class Hamacher(Tnorm):
    def compute(self, a, b):
        return fz.Hama(a,b)

class Product(Tnorm):
    def compute(self, a, b):
        return a*b

class Transition:
    def __init__(self, s0, s1, act, constr, vt):
        self.s0 = s0
        self.s1 = s1
        self.act = act
        self.constr = constr
        self.vt = vt
    def FV(self):
        return set.union(self.act.FV(),
                         self.constr.FV(),
                         self.vt.FV())

        
class Automata:
    def __init__(self, tnorm, varlist, states, inistate, transitions):
        self.tnorm = tnorm
        self.varlist = varlist
        self.states = states
        self.inistate = inistate
        self.transitions = transitions
    def FV(self):
        return set().union(*[t.FV() for t in self.transitions])

class Input:
    def __init__(self, name, varlist):
        self.name = name
        self.varlist = varlist
    def FV(self):
        return set()
    def match(self, act):
        if act.is_output():
            return None
        assert len(self.varlist) == len(act.vals)
        return {Var(name):val for name,val in zip(self.varlist, act.vals)}
    def get_str(self, match, varstate):
        vals = [str(match[Var(it)]) for it in self.varlist]
        return '?'+self.name+'('+', '.join(vals)+')'
    
class Output:
    def __init__(self, name, exprs):
        self.name = name
        self.exprs = exprs
    def FV(self):
        return set().union(*[e.FV() for e in self.exprs])
    def match(self, act):
        if act.is_input():
            return None
        elif act.name == None:
            return {}
        elif act.name == self.name:
            return {}
        else:
            return None
    def get_str(self, match, varstate):
        vals = [str(it.assign(varstate).eval()) for it in self.exprs]
        return '!'+self.name+'('+', '.join(vals)+')'

    
# class ExecutionState:
#     def __init__(self, states):
#         self.states = states

# def actionStep(automa, act, confiDic, variDic):  # ????
#     """
#     automa: model
#     act: action name
#     confiDic: dictionary mapping states to confidence values
#     variDic: dictionary mapping variable names to values 
#                 ---- actionState        ( JUST ACTION VARIABLES )
#     """
# #    actionDic = actionDic(automa)  # ????
#     newConfi = {k:0.0 for k in confiDic}
#     deciDic = {k:None for k in confiDic}
#     for tr in automa.tr:
#         if tr.act == act:
#             if Hama(Ceval(Csubst2(tr.constr, variDic)), confiDic[tr.s1]) > newConfi[tr.s2]: # asdfjhieuwhfaisen
#                 newConfi[tr.s2] = Hama(Ceval(Csubst2(tr.constr, variDic)), confiDic[tr.s1])
#                 deciDic[tr.s2] = tr
#     return newConfi, deciDic # los ! tienen C true, los ? tienen vartrans id
        
class ExecutionSequence:
    def __init__(self, automata, inistate, inivarstate):
        self.v = [{inistate:{'eps':1,'varstate':inivarstate, 'prevstate':None, 'action_str':None }}]
        self.automata = automata
        self.alive = True
        self.last_consolidated = 0
    def step(self, tact):
        prev = self.v[-1]
        next = {}
        for tr in self.automata.transitions:
            match = tr.act.match(tact)
            if match == None:
                continue
            conf = tr.constr.assign(match).eval()
            if tr.s0 not in prev:
                continue
            goc = self.automata.tnorm.compute(conf,
                                              prev[tr.s0]['eps'])
            if tr.s1 not in next or next[tr.s1]['eps'] < goc:
                environment = prev[tr.s0]['varstate']
                for it in match:
                    environment[it] = match[it]
                next[tr.s1] = {}
                next[tr.s1]['eps'] = goc
                next[tr.s1]['varstate'] = tr.vt.apply(environment)
                next[tr.s1]['prevstate'] = tr.s0
                next[tr.s1]['action_str'] =  tr.act.get_str(match,prev[tr.s0]['varstate'])
        self.v = self.v + [next]
        if next == {}:
            self.alive = False
        if len(next) == 1:
            self.last_consolidated = len(self.v)-1
    def __str__(self):
        return '\n\n'.join(['\n'.join(
            [str(k)+':'+', '.join(
                [str(kk)+':'+str(it[k][kk]) for kk in it[k]]) for k in it]) for it in self.v])
        
class OutputLog: # array? # MEJOR QUE SEA UN SET
    pass

# class VariableState:
#     pass # posiblemente sea un diccionario suelto

# class Trace:
#     pass # admitimos ! como test action

class AutomatonContext: #    pass # enabled, tracecontexts, hash
    def __init__(self, tracecontexts=[]):
        self.tracecontexts = tracecontexts

class TraceContext:
    def __init__(self, exe, selstate, automata, upcoming_sequence):
        self.exe = exe
        self.selstate = selstate
        self.automata = automata
        self.upcoming_sequence = upcoming_sequence
        #        pass # executionsequence, selectedstate, automatoncontext, upcoming_sequence
    
classes = {'Addition':Addition,
           'Subtraction':Subtraction,
           'Multiplication':Multiplication,
           'Division':Division,
           'Var':Var,
           'Val':Val,
           'Input':Input,
           'Output':Output,
           'Product':Product,
           'Hamacher':Hamacher,
           'GeqRel':GeqRel,
           'EqRel':EqRel,
           'LeqRel':LeqRel,
           'IntervalRel':IntervalRel,
           'TrueConstraint':TrueConstraint,
           'Conjunction': Conjunction,
           'Transition': Transition,
           'Automata': Automata,
           'VariableTransform':VariableTransform,
           'VariableTransforms':VariableTransforms}

class TestInput:
    def __init__(self, name, vals):
        self.name = name
        self.vals = vals
    def is_input(self):
        return True
    def is_output(self):
        return False
        
class TestOutput:
    def __init__(self, name):
        self.name = name
    def is_input(self):
        return False
    def is_output(self):
        return True

ttclasses = {'TestInput':TestInput, 'TestOutput':TestOutput}

ep = gr.AutomataParser(classes)
tp = gr.TestTraceParser(ttclasses)
# d = """HAMACHER
# X,Y,Z
# s0,s1,s2,s3
# s0
# s0,s1
# !O1 X*9
# HAMACHER
# X<=4 [0.62]
# Identity
# s0,s2
# ?Input2 X,Y,Z
# HAMACHER true
# X=Y*Z/3, Y=0
# s0,s3
# !O1 X*9
# HAMACHER
# X<=4 [0.62]
# Identity
# s0,s3
# ?Input2 X,Y,Z
# HAMACHER
# Y=X+1 [0.2], Z<=5<=X [0.7]
# X=Y*Z/3, Y=0"""
# ex = ep.parse_automata(d)
#ex = ep.parse_automata("5+5-5*8/8")
#res ='Addition(x,Addition(Subtraction(5.0,y),Subtraction(Multiplication(y,2.0),Division(f,2.0))))'
#assert str(ep.parse_automata('x+5-y+y*2-f/2')) == res



# def applyTrace(trace, automa, inistate):  # ??????
#     tra = trace2list(trace)
#     confiDic = {}
#     stDic = stateDic(automa)
#     for tr in automa.tr:
#         confiDic[tr.s1] = 0.0
#         confiDic[tr.s2] = 0.0
#     confiDic[inistate] = 1.0
#     for t in tra:
#         variDic = actionState( stDic[t.act],  # NECESITO DICCIONARIO ACCIONES LISTA DE VARIABLES :DONE:
#                               constlist2list(t.const))
#         # LO SIGUIENTE ES PROBAR LAS CONFIANZAS :NEXTACTION:
#         confiDic, uuu = actionStep(automa, t.act, confiDic, variDic)
#     return confiDic


# def automata2dot(autom): # RENDERTODOT
#     res = "digraph automata {"
#     for tr in autom.tr:
#         res = res + '"'+tr.s1+'" -> "'+tr.s2 + \
#         '" [label="'+tr.act+varlist2string(tr.args)+ \
#         '\\n'+C2string(tr.constr) + \
#         ('' if tr.vtran.head == None else
#          '\\n' + (vt2string(tr.vtran)) )+ \
#         '"]\n'
#     return res + "}"

