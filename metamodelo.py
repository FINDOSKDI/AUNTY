""" TODO:
* Construir las listas desde el modelo
"""
""" Observaciones:
* Hay dificultades relativas a la sobrecarga de acciones.
No habra sobrecarga de acciones.


"""
from textx import metamodel_from_str
from copy import copy
from types import SimpleNamespace
from fuzzy import *
from metamodel.grammar import *


def tname(obj): # MUY DEPRECATED
    return obj.__class__.__name__


def vt2list(vt): #MUY DEPRECATED
    if vt.head == None:
        return []
    else:
        return [vt.head]+[a.head for a in vt.tail]

def varlist2list(varlist): #MUY DEPRECATED
    if varlist.head == None:
        return []
    else:
        return [varlist.head.name]+[a.head.name for a in varlist.tail]


def varlistFV(varlist): #FV
    return set(varlist2list(varlist))

def VTFV(vt): #FV
    return set([t.v.name for t in vt2list(vt)]+[t.c.name for t in vt2list(vt) if tname(t.c) == 'V'])

def TFV(t): # FV
    if tname(t) == 'R':
        return set()
    else:
        return set([t.name])

def CFV(C): # FV
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

def Tsubst(T, vari, valu): # SUBS
    T = copy(T)
    if tname(T) == 'V' and T.name == vari:
        T.value = valu
    return T
    
def Csubst(C, vari, valu): # SUBS
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

def Csubst2(C, state): # SUBS
    C = copy(C)
    for k in state.keys():
        if k in CFV(C):
            C = Csubst(C,k,state[k])
    return C


def Ceval(C): # EVAL
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

    
    
def transicionFV(transicion): #FV #UNUSED
    return varlistFV(transicion.args ).union( VTFV(transicion.vtran) ).union( CFV(transicion.constr) )

def Tstr(t): # STR
    if tname(t) == 'R':
        return str(t.value)
    else:
        return t.name

    
def vt2string(vt): #STR
    return "["+str.join(",",[Tstr(t.c)+"/"+Tstr(t.v) for t in vt2list(vt)])+"]"

def C2string(C): #STR
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
    

def varlist2string(varlist): # STR
    return "("+str.join(",",varlist2list(varlist))+")"


def trace2list(trace): # MUY DEPRECATED     
    return [SimpleNamespace(act=trace.act,const=trace.const)] + trace.tail 

def constlist2list(constlist): # MUY DEPRECATED
    if constlist.head == None:
        return []
    return [constlist.head] + [c.head for c in constlist.tail]

def actionState(varlistlist, constlistlist): # ??????
    dic = {}
    vl = varlistlist
    cl = constlistlist
    for a,b in zip(vl,cl):
        dic[a] = b.value
    return dic


def applyTrace(trace, automa, inistate):  # ??????
    tra = trace2list(trace)
    confiDic = {}
    stDic = stateDic(automa)
    for tr in automa.tr:
        confiDic[tr.s1] = 0.0
        confiDic[tr.s2] = 0.0
    confiDic[inistate] = 1.0
    for t in tra:
        variDic = actionState( stDic[t.act],  # NECESITO DICCIONARIO ACCIONES LISTA DE VARIABLES :DONE:
                              constlist2list(t.const))
        # LO SIGUIENTE ES PROBAR LAS CONFIANZAS :NEXTACTION:
        confiDic, uuu = actionStep(automa, t.act, confiDic, variDic)
    return confiDic


def automata2dot(autom): # RENDERTODOT
    res = "digraph automata {"
    for tr in autom.tr:
        res = res + '"'+tr.s1+'" -> "'+tr.s2 + \
        '" [label="'+tr.act+varlist2string(tr.args)+ \
        '\\n'+C2string(tr.constr) + \
        ('' if tr.vtran.head == None else
         '\\n' + (vt2string(tr.vtran)) )+ \
        '"]\n'
    return res + "}"




def automatonStates(automa): #GETSTATES
    return set([t.s1 for t in automa.tr]).union(set([t.s2 for t in automa.tr]))


def stateDic(automa):  #GETACTIONASSOCIATEDVARIABLES
    res = {}
    for tr in automa.tr:
        res[tr.act] = varlist2list(tr.args)
    return res

def actionDict(automa): #GETACTIONASSOCIATEDVARIABLES
    dic = {}
    for t in automa.tr:
        dic[t.act] = varlist2list(t.args)
    return dic

def outgoingDict(automa): #GETSTATEOUTGOINGTRANSITIONS
    dic = {t:[] for t in automatonStates(automa)}
    for t in automa.tr:
        dic[t.s1] = dic[t.s1] + [t]
    return dic

def ingoingDict(automa):#GETSTATEINGOINGTRANSITIONS
    dic = {t:[] for t in automatonStates(automa)}
    for t in automa.tr:
        dic[t.s2] = dic[t.s2] + [t]
    return dic

def actionStep(automa, act, confiDic, variDic):  # ????
    """
    automa: model
    act: action name
    confiDic: dictionary mapping states to confidence values
    variDic: dictionary mapping variable names to values 
                ---- actionState        ( JUST ACTION VARIABLES )
    """
#    actionDic = actionDic(automa)  # ????
    newConfi = {k:0.0 for k in confiDic}
    deciDic = {k:None for k in confiDic}
    for tr in automa.tr:
        if tr.act == act:
            if Hama(Ceval(Csubst2(tr.constr, variDic)), confiDic[tr.s1]) > newConfi[tr.s2]: # asdfjhieuwhfaisen
                newConfi[tr.s2] = Hama(Ceval(Csubst2(tr.constr, variDic)), confiDic[tr.s1])
                deciDic[tr.s2] = tr
                
    return newConfi, deciDic # los ! tienen C true, los ? tienen vartrans id


# =============== EXAMPLES AND TESTS ==================

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
tracestr = """(?asds(55))"""


mm = metamodel_from_str(grammar)
model = mm.model_from_str(automstr)
tr = model.tr

tmm =metamodel_from_str(tracegrammar)
tmodel = tmm.model_from_str(tracestr)





def test_prueba1():
    automataprueba1 = mm.model_from_str("""
    s1, ?foo(x), (4.0 <= x <= 5.0)^0.5, [], s1;
    """)
    trazaprueba1 = tmm.model_from_str("""
    (?foo(3.75))
    """)
#    C = Csubst2(automataprueba1.tr[0].constr, {'x':1.5})
#    print(2 <C.t2.value)
    x = applyTrace(trazaprueba1, automataprueba1, 's1')
    print(x)


if __name__ == "__main__":
    test_prueba1()
