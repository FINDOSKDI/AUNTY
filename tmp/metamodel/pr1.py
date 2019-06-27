from textx import metamodel_from_str

grammar = """
Entity : e*=Letter;
Mod : Entity;
Letter : c=AA | c=BB;
AA : c='a';
BB : c='b';
A : 'a';
B : 'b';
"""

class Mod:
    def __init__(self):
        pass
class AA:
    def __init__(self, parent, c):
        def _valuestr():
            return c
        self.valuestr = _valuestr
class BB:
    def __init__(self, parent, c):
        def _valuestr():
            return c
        self.valuestr = _valuestr
        
class AB:
    def __init__(self, c):
        self.valuestr = c.valuestr
    def __str__(self):
        return self.valuestr()
    
class Letter:
    def __init__(self,parent, c):#  l, t):
        self.parent = parent
        self.c = AB(c)
       # self.l = l
       # self.t = t
    def __str__(self):
        return str(self.c)
    
class Entity:
    def __init__(self, e):
        self.e = e

        
mm = metamodel_from_str(grammar, classes=[Letter, Entity, AA, BB])

model = mm.model_from_str("ba")
