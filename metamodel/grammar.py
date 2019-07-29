from textx import metamodel_from_str

grammar = """
Automaton : tr*= Transicion ;
C    : 'True' | B | T | Compo ;
Compo : '(' c1=C tnorm=Tnorm c2=C ')' ; 
Transicion: s1=ID ',' act=Action args=Varlist ',' 
            constr=C ',' vtran=VT ',' s2=ID ';' ;
Term : V | R;
V    : name=ID | 'value=' value=FLOAT;
R    : value=FLOAT | 'name=' name=ID;
B    : Bleq | Bgeq | Beq;
Bleq : '(' t1=Term '<=' t2=Term ')^' delta=FLOAT ;
Bgeq : '(' t1=Term '>=' t2=Term ')^' delta=FLOAT ;
Beq  : '(' t1=Term '==' t2=Term ')^' delta=FLOAT ;
T    : '(' t1=Term '<=' t2=Term '<=' t3=Term ')^' delta=FLOAT ;
Tnorm: 'Luka' | 'Gode' | 'Prod' | 'Hama';
VT   : '[' ']' | '[' head=Trans tail*=TransTail ']' ;
TransTail : ',' head=Trans;
Trans     : c=Term '/' v=V;
Varlist   : '(' ')' | '(' head=V tail*=VarTail ')';
VarTail   : ',' head=V;
Action    : '?' ID | '!' ID;
"""
tracegrammar = """
Trace : '(' act=Action const=Constlist  ')' tail*=TraceTail;
TraceTail : ',' '(' act=Action const=Constlist  ')';
Action    : '?' ID | '!' ID;
Constlist : '(' head=R tail*=ConstTail ')' | '()'; 
ConstTail : ',' head=R;
R    : value=FLOAT;
"""
alttracegrammar = """
Trace : acts*=Action[',' eolterm];
Action: Input | Output;
Input: '?' name=ID '(' vals*=FLOAT[',' eolterm] ')';
Output: '!' (name=ID)?;
"""

class TestTraceParser:
    def __init__(self, classes):
        self.classes = classes

        class Trace:
            def __init__(self, acts):
                self.acts = acts
            def abstract_syntax(self):
                return [it.abstract_syntax() for it in self.acts]
        self.Trace = Trace

        class Input:
            def __init__(self, parent, name, vals):
                self.parent = parent
                self.name = name
                if vals == None:
                    self.vals = []
                else:
                    self.vals = vals
            def abstract_syntax(self):
                return classes['TestInput'](self.name, self.vals)
        self.Input = Input       

        class Output:
            def __init__(self, parent, name):
                self.parent = parent
                self.name = name
                print(self.name)
            def abstract_syntax(self):
                return classes['TestOutput'](self.name)
        self.Output = Output

    def parse_test_trace(self, test_trace_str):

        alttesttracegrammar = ("Trace : acts*=Action[',' eolterm];"
                               "Action: Input | Output;"
                               "Input: '?' name=ID '(' vals*=FLOAT[',' eolterm] ')';"
                               "Output: '!' (name=ID)?;")

        
        listclasses = [self.Trace, self.Input, self.Output]
        
        mm = metamodel_from_str(alttesttracegrammar, classes=listclasses)
        return mm.model_from_str(test_trace_str).abstract_syntax()



        
class AutomataParser:
   
    def __init__(self, classes):
        # self.Addition = classes['Addition']
        # self.Subtraction = classes['Subtraction']
        # self.Multiplication = classes['Multiplication']
        # self.Division = classes['Division']
        # self.Vr = classes['Vr']
        # self.Vl = classes['Vl']
        # self.VariableTransform = classes['VariableTransform']
        # self.VariableTransforms = classes['VariableTransforms']
        self.classes = classes

        
        class Input:
            def __init__(self, parent, name, varlist):
                self.parent = parent
                self.name = name
                self.varlist = varlist
            def abstract_syntax(self):
                return classes['Input'](self.name, self.varlist)
        self.Input = Input
        
        class Output:
            def __init__(self, parent, name, exprs):
                self.parent = parent
                self.name = name
                self.exprs = exprs
            def abstract_syntax(self):
                return classes['Output'](self.name, [e.abstract_syntax() for e in self.exprs])
        self.Output = Output
        
        """ Constraint: ctype=BinRel | ctype=TerRel;
        BinRel: l=Expression ctype='<=' r=Expression '['delta=FLOAT']' |
        l=Expression ctype='='  r=Expression '['delta=FLOAT']' |
        l=Expression ctype='>=' r=Expression '['delta=FLOAT']';
        TerRel: first=Expression '<=' second=Expression '<=' third=Expression '['delta=FLOAT']';
        """
        # class Constraint:
        #     def __init__(self, parent, ctype):
        #         self.parent = parent
        #         self.ctype = ctype
        #     def abstract_syntax(self):
        #         pass
        # self.Constraint = Constraint

        class BinRel:
            def __init__(self, parent, l, ctype, r, delta):
                self.parent = parent
                self.l = l
                self.ctype = ctype
                self.r = r
                self.delta = delta
            def abstract_syntax(self):
                if self.ctype == '<=':
                    return classes['LeqRel'](self.l.abstract_syntax(), self.r.abstract_syntax(), self.delta)
                elif self.ctype == '=':
                    return classes['EqRel'](self.l.abstract_syntax(), self.r.abstract_syntax(), self.delta)
                else: # self.ctype == '>='
                    return classes['GeqRel'](self.l.abstract_syntax(), self.r.abstract_syntax(), self.delta)
        self.BinRel = BinRel

        class TerRel:
            def __init__(self, parent, first, second, third, delta):
                self.parent = parent
                self.first = first
                self.second = second
                self.third = third
                self.delta = delta
            def abstract_syntax(self):
                return classes['IntervalRel'](self.first.abstract_syntax(),
                                              self.second.abstract_syntax(),
                                              self.third.abstract_syntax(),
                                              self.delta)
        self.TerRel = TerRel
        
        class TrueConstraint:
            def __init__(self, parent, string):
                self.parent = parent
                self.string = string
            def abstract_syntax():
                return classes['TrueConstraint']()
        self.TrueConstraint = TrueConstraint

        #"Transition: from=ID ',' to=ID act=Action tnorm=Tnorm constrs=Constraints vt=VTransforms;"   #
        class Transition:
            def __init__(self, parent, s0, s1, act, tnorm, constrs, vt):
                self.s0 = s0
                self.s1 = s1
                self.act = act
                self.tnorm = tnorm
                self.constrs = constrs
                self.vt = vt
            def abstract_syntax(self):
                if self.constrs.constr == None:
                    if len(self.constrs.constrs) == 1:
                        constr = self.constrs.constrs[0].abstract_syntax()
                    else:
                        acu = self.constrs.constrs[0].abstract_syntax()
                        for i in self.constrs.constrs[1:]:
                            acu = classes['Conjunction'](acu, self.tnorm.abstract_syntax(), i.abstract_syntax())
                        constr = acu
                else:
                    constr = TrueConstraint.abstract_syntax()
                return classes['Transition'](self.s0, self.s1,
                                             self.act.abstract_syntax(),
                                             constr, self.vt.abstract_syntax())
        self.Transition = Transition

        # "Automata: tnorm=Tnorm varlist=Vars states=States inistate=ID transitions*=Transition;"         #        
        class Automata:
            def __init__(self, tnorm, varlist, states, inistate, transitions):
                self.tnorm = tnorm
                self.varlist = varlist
                self.states = states
                self.inistate = inistate
                self.transitions = transitions
            def abstract_syntax(self):
                return classes['Automata'](self.tnorm.abstract_syntax(),
                                           self.varlist.vlist,
                                           self.states.slist,
                                           self.inistate,
                                           [t.abstract_syntax() for t in self.transitions])
        self.Automata = Automata
                         
        class Product:
            def __init__(self, parent, string):
                self.parent = parent
                self.string = string
            def abstract_syntax(self):
                return classes['Product']()
        self.Product = Product

        class Hamacher:
            def __init__(self, parent, string):
                self.parent = parent
                self.string = string
            def abstract_syntax(self):
                return classes['Hamacher']()
        self.Hamacher = Hamacher
        
        class VTransforms:
            def __init__(self, parent, vtransfms, ctype):
                self.parent = parent
                self.ctype = ctype
                self.vtransfms = vtransfms
            def abstract_syntax(self):
                if self.ctype == 'Identity':
                    return classes['VariableTransforms']()
                else:
                    return classes['VariableTransforms']([it.abstract_syntax() for it in self.vtransfms])
        self.VTransforms = VTransforms

        class VTransform:
            def __init__(self, parent, var, expr):
                self.parent = parent
                self.var = var
                self.expr = expr
            def abstract_syntax(self):
                return classes['VariableTransform'](self.var, self.expr.abstract_syntax())
        self.VTransform = VTransform
        
        def left_associative_op(ctype, l, r, op):
            if ctype != None and ctype != []:
                acu = op(l.abstract_syntax(), r[0].abstract_syntax())
                for i in r[1:]:
                    acu = op(acu, self.i.abstract_syntax())
                return acu
            else:
                return l.abstract_syntax()
            
        # '+'    
        class Expression1:
            def __init__(self, parent, l, ctype, r):
                self.parent = parent
                self.l = l
                self.ctype = ctype
                self.r = r
            def abstract_syntax(self):
                return left_associative_op(self.ctype, self.l, self.r, classes['Addition'])
        self.Expression1 = Expression1
        
        # '-'
        class Expression2:
            def __init__(self, parent, l, ctype, r):
                self.parent = parent
                self.l = l
                self.ctype = ctype
                self.r = r
            def abstract_syntax(self):
                return left_associative_op(self.ctype, self.l, self.r, classes['Subtraction'])
        self.Expression2 = Expression2
        
        # '*'        
        class Expression3:
            def __init__(self, parent, l, ctype, r):
                self.parent = parent
                self.l = l
                self.ctype = ctype
                self.r = r
            def abstract_syntax(self):
                return left_associative_op(self.ctype, self.l, self.r, classes['Multiplication'])
        self.Expression3 = Expression3

        # '/'        
        class Expression4:
            def __init__(self, parent, l, ctype, r):
                self.parent = parent
                self.l = l
                self.ctype = ctype
                self.r = r
            def abstract_syntax(self):
                return left_associative_op(self.ctype, self.l, self.r, classes['Division'])
        self.Expression4 = Expression4

        # '()', terms        
        class Expression5:
            def __init__(self, parent, ins, ctype):
                self.parent = parent
                self.ins = ins
                self.ctype = ctype
            def abstract_syntax(self):
                if self.ctype == None or self.ctype == []:
                    return self.ins.abstract_syntax()
                else:
                    return self.ctype.abstract_syntax()
        self.Expression5 = Expression5

        class Term:
            def __init__(self, parent, ctype):
                self.parent = parent
                self.ctype = ctype
            def abstract_syntax(self):
                return self.ctype.abstract_syntax()
        self.Term = Term

        class Var:
            def __init__(self, parent, var, indexlist):
                self.parent = parent
                self.var = var
                if indexlist == None:
                    self.indexlist = []
                else:
                    self.indexlist = indexlist
            def abstract_syntax(self):
                return classes['Var'](self.var, self.indexlist)
        self.Var = Var
            
        class Val:
            def __init__(self, parent, val):
                self.parent = parent
                self.val = val
            def abstract_syntax(self):
                return classes['Val'](self.val)
        self.Val = Val

        
        
    def parse_automata(self, model_str):
        # exprgrammar = ("S: e=Expression1;"                          # HAY QUE CAMBIAR ESTO
        #                "Expression1:       l=Expression2 (ctype='+' r=Expression1)*;"
        #                "Expression2:       l=Expression3 (ctype='-' r=Expression2)*;"
        #                "Expression3:       l=Expression4 (ctype='*' r=Expression3)*;"
        #                "Expression4:       l=Expression5 (ctype='/' r=Expression4)*;"
        #                "Expression5:      ctype=Term | '(' ins=Expression1 ')';"
        #                "Term: ctype=Var | ctype=Val;"
        #                "Var: var=ID;"
        #                "Val: val=FLOAT;")



        altgrammar = ("Automata: tnorm=Tnorm varlist=Vars states=States inistate=ID transitions*=Transition;"      # DONE
                      "Tnorm: Product | Hamacher;"                                                                 # DONE
                      "Product: string=/PRODUCT|Product|product/ ;"                                                # DONE
                      "Hamacher: string=/HAMACHER|Hamacher|hamacher/ ;"                                            # DONE
                      "Vars: /\s*/ vlist*=ID[',' eolterm];"                                                         # DONE
                      "States: /\s*/ slist*=ID[',' eolterm];"                                                       # DONE
                      "Transition: s0=ID ',' s1=ID act=Action tnorm=Tnorm constrs=Constraints vt=VTransforms;"     # DONE
                      "Action: Input | Output;"                                                                    # DONE
                      "Input: '?' name=ID varlist*=ID[',' eolterm];"                                               # DONE
                      "Output: '!' name=ID exprs*=Expression[',' eolterm];"                                        # DONE
                      "Expression: Expression1;"                                                                   # DONE
                      "Expression1:       l=Expression2 (ctype='+' r=Expression1)*;"                               # DONE
                      "Expression2:       l=Expression3 (ctype='-' r=Expression2)*;"                               # DONE
                      "Expression3:       l=Expression4 (ctype='*' r=Expression3)*;"                               # DONE
                      "Expression4:       l=Expression5 (ctype='/' r=Expression4)*;"                               # DONE
                      "Expression5:      ctype=Term | '(' ins=Expression1 ')';"                                    # DONE
                      "Term: ctype=Var | ctype=Val;"                                                               # DONE
                      "Var: var=ID ('['indexlist+=INT[',' eolterm]  ']')?  ;"                                      # DONE
                      "Val: val=FLOAT;"                                                                            # DONE
                      "TrueConstraint: string=/TRUE|True|true/;"                                                   # DONE
                      "Constraints:  /\s*/ constrs+=Constraint[',' eolterm] |   constr=TrueConstraint;"            # DONE
                      "Constraint: BinRel | TerRel;"                                                               # DONE
                      "BinRel: l=Expression ctype='<=' r=Expression '['delta=FLOAT']' |"                           # DONE
                      "l=Expression ctype='='  r=Expression '['delta=FLOAT']' |"                                   # DONE
                      "l=Expression ctype='>=' r=Expression '['delta=FLOAT']';"                                    # DONE
                      "TerRel: first=Expression '<=' second=Expression '<=' third=Expression '['delta=FLOAT']';"   # DONE
                      "VTransform:  var=ID '=' expr=Expression ;"                                                  # DONE
                      "VTransforms:     /\s*/ vtransfms+=VTransform[',' eolterm] | ctype='Identity';")             # DONE
        
        listclasses = [self.VTransforms,
                       self.VTransform,
                       self.Automata,
                       self.Transition,
                       self.Input,
                       self.Output,
                       self.Product,
                       self.Hamacher,
                       self.TrueConstraint,
                       self.BinRel,
                       self.TerRel,
                       self.Expression1,
                       self.Expression2,
                       self.Expression3,
                       self.Expression4,
                       self.Expression5,
                       self.Term,
                       self.Var,
                       self.Val]
        
        mm = metamodel_from_str(altgrammar, classes=listclasses)
        return mm.model_from_str(model_str).abstract_syntax()


def test_expr():
    global expr
    expr = mm.model_from_str('5+5-5*8/8')
    return expr
    

def test_1():
    from textx import metamodel_from_str
    mm = metamodel_from_str(altgrammar, classes=listclasses)
    d = """GODEL
X,Y,Z
s0,s1,s2,s3
s0
s0,s1
!O1 x*9
HAMACHER
X<=4 [0.62]
Identity
s0,s2
?Input2 X,Y,Z
GODEL true
X=Y*Z/3, Y=0
s0,s3
!O1 x*9
HAMACHER
X<=4 [0.62]
Identity
s0,s3
?Input2 X,Y,Z
GODEL
Y=X+1 [0.2], Z<=5<=X [0.7]
X=Y*Z/3, Y=0"""
    mm.model_from_str(d)
    
def test_2():
    from textx import metamodel_from_str
    mmt = metamodel_from_str(alttracegrammar)
    
def test_3():
    from textx import metamodel_from_str
    mmtt = metamodel_from_str(alttesttracegrammar)


