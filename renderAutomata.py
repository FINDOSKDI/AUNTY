#!/usr/bin/env python
import sys
import pygraphviz as pgv
from metamodelo import *

with open(sys.argv[1], 'r') as f:
    au = str(f.read())

stri = automata2dot(mm.model_from_str(au))
with open(sys.argv[2]+'.source', 'w') as f:
    f.write(stri)

G = pgv.AGraph(stri)
G.draw(sys.argv[2], prog='dot')
