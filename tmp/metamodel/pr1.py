from textx import metamodel_from_str

grammar = """
Mod : Entity;
Entity : e*=Letter;
Letter : t=AA | l=BB;
AA : t=A;
BB : l=B;
A : 'a';
B : 'b';
"""

class Mod:
    def __init__(self):
        pass
class Letter:
    def __init__(self,parent,  l, t):
        self.l = l
        self.t = t
    def __str__(self):
        return parent

class Entity:
    def __init__(self, e):
        self.e = e

        
mm = metamodel_from_str(grammar, classes=[Letter])

model = mm.model_from_str("ba")
