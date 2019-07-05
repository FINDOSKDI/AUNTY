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
altgrammar = """
Automata: tnorm=Tnorm vars=Vars states=States inistate=ID transitions*=Transition;
Tnorm: type=Godel | type=Hamacher;
Godel: str=/GODEL|Godel|godel/ ;
Hamacher: str=/HAMACHER|Hamacher|hamacher/ ;
Vars: /\s*/ list*=ID[',' eolterm];
States: /\s*/ list*=ID[',' eolterm];
Transition: from=ID ',' to=ID act=Action tnorm=Tnorm constrs=Constraints vt=VTransforms;
Action: Input | Output;
Input: '?' name=ID vars*=ID[',' eolterm];
Output: '!' name=ID exprs*=Expression[',' eolterm];
Expression: Expression1;
Expression1:       l=Expression2 (type='+' r=Expression1)*;
Expression2:       l=Expression3 (type='-' r=Expression2)*;
Expression3:       l=Expression4 (type='*' r=Expression3)*;
Expression4:       l=Expression5 (type='/' r=Expression4)*;
Expression5:      type=Term | '(' in=Expression1 ')';
Term: type=Var | type=Val;
Var: var=ID;
Val: val=FLOAT;
True: str=/TRUE|True|true/;
Constraints:  /\s*/ constrs+=Constraint[',' eolterm] |   constrs=True;
Constraint: type=BinRel | type=TerRel;
BinRel: l=Expression type='<=' r=Expression '['delta=FLOAT']' |
        l=Expression type='='  r=Expression '['delta=FLOAT']' |
        l=Expression type='>=' r=Expression '['delta=FLOAT']';
TerRel: first=Expression '<=' second=Expression '<=' third=Expression '['delta=FLOAT']';
VTransform:  var=ID '=' expr=Expression ;
VTransforms:     /\s*/ vtransfms+=VTransform[',' eolterm] | type='Identity';
"""


expregrammar = """Expression1:       l=Expression2 (type='+' r=Expression1)*;
Expression2:       l=Expression3 (type='-' r=Expression2)* ;
Expression3:       l=Expression4 (type='*' r=Expression3)* ;
Expression4:       l=Expression5 (type='/' r=Expression4)* ;
Expression5:      type=Term | '(' in=Expression1 ')';
Term: type=Var | type=Val;
Var: var=ID;
Val: val=FLOAT;"""

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


testgrammar = """Constraints: type='TRUE' | constrs*=Constraint[',' eolterm];
Expression: Expression1;
Expression1:       l=Expression2 (type='+' r=Expression1)*;
Expression2:       l=Expression3 (type='-' r=Expression2)*;
Expression3:       l=Expression4 (type='*' r=Expression3)*;
Expression4:       l=Expression5 (type='/' r=Expression4)*;
Expression5:      type=Term | '(' in=Expression1 ')';
Term: type=Var | type=Val;
Var: var=ID;
Val: val=FLOAT;

Constraint: type=BinRel | type=TerRel;
BinRel: l=Expression type='<=' r=Expression '['delta=FLOAT']';

TerRel: first=Expression '<=' second=Expression '<=' third=Expression '['delta=FLOAT']';"""

def test_1():
    from textx import metamodel_from_str
    mm = metamodel_from_str(altgrammar)
    mm.model_from_str(d)
