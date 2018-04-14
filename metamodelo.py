from textx import metamodel_from_str
from copy import copy

def tname(obj):
    return obj.__class__.__name__

def fuzzyleq(y,delta):
    return lambda x: 1 if x <= y else \
	0 if x > y + delta else \
	1 - (x - y) / delta

def fuzzyor(lam1, lam2):
    return lambda x: max([lam1(x), lam2(x)])

def fuzzyand(lam1, lam2):
    return lambda x: min([lam1(x), lam2(x)])

def fuzzynot(lam1):
    return lambda x: 1 - lam1(x)
def fuzzyeq(x,y,delta):
    return min([fuzzyleq(y,delta)(x), fuzzyleq(x,delta)(y)])
def fuzzygeq(z,delta):
    return fuzzynot(fuzzyleq(z-delta,delta))

def fuzzyinterval(y,z,delta):
    return fuzzyand(fuzzyleq(y,delta),fuzzygeq(z,delta))


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


def vt2list(vt):
    if vt.head == None:
        return []
    else:
        return [vt.head]+[a.head for a in vt.tail]

def varlist2list(varlist):
    if varlist.head == None:
        return []
    else:
        return [varlist.head.name]+[a.head.name for a in varlist.tail]


def varlistFV(varlist):
    return set(varlist2list(varlist))

def VTFV(vt):
    return set([t.v.name for t in vt2list(vt)]+[t.c.name for t in vt2list(vt) if tname(t.c) == 'V'])

def TFV(t):
    if tname(t) == 'R':
        return set()
    else:
        return set([t.name])

def CFV(C):
    if C == 'True':
        return set()
    if tname(C) == 'Bleq':
        return  TFV(C.t1).union(TFV(C.t2))
    if tname(C) == 'Beq':
        return  TFV(C.t1).union(TFV(C.t2))
    if tname(C) == 'Bgeq':
        return  TFV(C.t1).union(TFV(C.t2))
    if tname(C) == 'T':
                return  TFV(C.t1).union(TFV(C.t2)).union(TFV(C.t3))
    if tname(C) == 'Compo':
        return CFV(C.c1).union( CFV(C.c2) )

def Tsubst(T, vari, valu):
    T = copy(T)
    if tname(T) == 'V' and T.name == vari:
        T.value = valu
    return T
    
def Csubst(C, vari, valu):
    C = copy(C)
    if C == 'True':
        return C
    if tname(C) == 'Bleq':
        C.t1 = Tsubst(C.t1, vari, valu)
        C.t2 = Tsubst(C.t2, vari, valu)
        return  C
    if tname(C) == 'Beq':
        C.t1 = Tsubst(C.t1, vari, valu)
        C.t2 = Tsubst(C.t2, vari, valu)
        return  C
    if tname(C) == 'Bgeq':
        C.t1 = Tsubst(C.t1, vari, valu)
        C.t2 = Tsubst(C.t2, vari, valu)
        return  C
    if tname(C) == 'T':
        C.t1 = Tsubst(C.t1, vari, valu)
        C.t2 = Tsubst(C.t2, vari, valu)
        C.t3 = Tsubst(C.t3, vari, valu)
        return  C
    if tname(C) == 'Compo':
        C.c1 = Csubst(C.c1, vari, valu)
        C.c2 = Csubst(C.c2, vari, valu)
        return C

def Csubst2(C, state):
    C = copy(C)
    for k in state.keys():
        if k in CFV(C):
            C = Csubst(C,k,state[k])
    return C

def Hama(a,b):
    return (a*b)/(a+b-a*b)

def Ceval(C):
    if C == 'True':
        return 1.0
    if tname(C) == 'Bleq':
        return  fuzzyleq(C.t2.value, C.delta)(C.t1.value)
    if tname(C) == 'Beq':
        return  fuzzyeq(C.t1.value, C.t2.value, C.delta)
    if tname(C) == 'Bgeq':
        return fuzzygeq(C.t2.value, C.delta)(C.t1.value)
    if tname(C) == 'T':
        return  fuzzyinterval(C.t3.value, C.t1.value, C.delta)(C.t2.value)
    if tname(C) == 'Compo':
        return Hama(Ceval(C.c1), Ceval(C.c2))

    
    
def transicionFV(transicion):
    return varlistFV(transicion.args ).union( VTFV(transicion.vtran) ).union( CFV(transicion.constr) )

def Tstr(t):
    if tname(t) == 'R':
        return str(t.value)
    else:
        return t.name

    
def vt2string(vt):
    return "["+str.join(",",[Tstr(t.c)+"/"+Tstr(t.v) for t in vt2list(vt)])+"]"

def C2string(C):
    if C == 'True':
        return C
    if tname(C) == 'Bleq':
        return  '('+ Tstr(C.t1)+ ' <= ' +Tstr(C.t2) + ')^' + str(C.delta)
    if tname(C) == 'Beq':
        return  '('+ Tstr(C.t1)+ ' == ' +Tstr(C.t2) + ')^' + str(C.delta)        
    if tname(C) == 'Bgeq':
        return  '('+ Tstr(C.t1) +' >= ' +Tstr(C.t2) + ')^' + str(C.delta)        
    if tname(C) == 'T':
        return  '('+ Tstr(C.t1)+ ' <= ' +Tstr(C.t2) + ' <= ' + Tstr(C.t3) + ')^' + str(C.delta)        
    if tname(C) == 'Compo':
        return "(" + C2string(C.c1) + " " + C.tnorm + " " + C2string(C.c2) + ")"
    

def varlist2string(varlist):
    return "("+str.join(",",varlist2list(varlist))+")"


tracegrammar = """
Trace : '(' act=Action const=Constlist  ')' tail*=TraceTail;
TraceTail : ',' '(' act=Action const=Constlist  ')';
Action    : '?' ID | '!' ID;
Constlist : '(' head=R tail*=ConstTail ')' | '()'; 
ConstTail : ',' head=R;
R    : value=FLOAT;
"""

def trace2list(trace):
    return [SimpleNamespace(act=trace.act,const=trace.const)] + trace.tail 

def constlist2list(constlist):
    if constlist.head == None:
        return []
    return [constlist.head] + [c.head for c in constlist.tail]

def actionState(varlist, constlist):
    dic = {}
    vl = varlist2list(varlist)
    cl = constlist2list(constlist)
    for a,b in zip(vl,cl):
        dic[a] = b
    return dic

automstr = """q38, ?endOfRecord(), True, [],  q115;
q42, ?noMorePendingRR(), True, [], q43;
q42, ?readRR(rr), True, [], q42;
q38, ?readBPM(bpm), (63.1 <= bpm <= 70.9)^3.9, [], q42;
q0, ?checkGender(gen), (gen == 0)^0, [], q1;
q37a, !recordAgeRange60to69(), True, [], q37b;
q1, ?checkAge(age), (60 <= age <= 69)^13, [GoC/branchGoC], q37a;
q37b, ?minute(m), True, [m/min], q38;
q38, ?readBPM(bpm), (bpm >= 70.9)^3.9, [], q39;
q38, ?readBPM(bpm), (bpm <= 63.1)^3.9, [], q39;
q39, ?readRR(rr), (rr >= 980)^84.5, [], q40;
q39, ?readRR(rr), (rr <= 811)^84.5, [], q40;
q39, ?readRR(rr), True, [], q39;
q43, !ok(min,GoC), True, [branchGoC/GoC], q37b;
q41, !recordAlarm(min,GoC), True, [branchGoC/GoC], q37b;
q40, ?noMorePendingRR(), True, [], q41;
q40, ?readRR(rr), True, [], q40;
q39, ?noMorePendingRR(), True, [], q43;
"""

def automata2dot(autom):
    res = "digraph automata {"
    for tr in autom.tr:
        res = res + '"'+tr.s1+'" -> "'+tr.s2 + \
        '" [label="'+tr.act+varlist2string(tr.args)+ \
        '\\n'+C2string(tr.constr) + \
        ('' if tr.vtran.head == None else
         '\\n' + (vt2string(tr.vtran)) )+ \
        '"]\n'
    return res + "}"

tracestr = """(?asds(55))"""


def automatonStates(automa):
    return set([t.s1 for t in automa.tr]).union(set([t.s2 for t in automa.tr]))

def actionDict(automa):
    dic = {}
    for t in automa.tr:
        dic[t.act] = varlist2list(args)
    return dic

def outgoingDict(automa):
    dic = {t:[] for t in automatonStates(automa)}
    for t in automa.tr:
        dic[t.s1] = dic[t.s1] + [t]
    return dic

def ingoingDict(automa):
    dic = {t:[] for t in automatonStates(automa)}
    for t in automa.tr:
        dic[t.s2] = dic[t.s2] + [t]
    return dic

def actionStep(automa, act, confiDic, variDic):
    actionDic = actionDic(automa)
    return


mm = metamodel_from_str(grammar)
model = mm.model_from_str(automstr)
tr = model.tr

