from textx import metamodel_from_str

def tname(obj):
    return obj.__class__.__name__

grammar = """
Automaton : tr*= Transicion ;
C    : 'True' | B | T | Compo ;
Compo : '(' c1=C tnorm=Tnorm c2=C ')' ; 
Transicion: s1=ID ',' act=Action args=Varlist ',' 
            constr=C ',' vtran=VT ',' s2=ID ';' ;

Term : V | R;
V    : name=ID;
R    : value=FLOAT;
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



def Tstr(t):
    if tname(t) == 'R':
        return str(t.value)
    else:
        return t.name

def vt2list(vt):
    if vt.head == None:
        return []
    else:
        return [vt.head]+[a.head for a in vt.tail]

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
    
def varlist2list(varlist):
    if varlist.head == None:
        return []
    else:
        return [varlist.head.name]+[a.head.name for a in varlist.tail]

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


automstr = """
q38, ?endOfRecord(), True, [],  q115;
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

tracestr = """(?asds(55))
"""

# exe = []

# trace = metamodel_from_str(tracegrammar).model_from_str(tracestr)


# for i in trace.tail:
#     pass



mm = metamodel_from_str(grammar)
model = mm.model_from_str(automstr)
tr = model.tr

