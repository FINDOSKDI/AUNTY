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
