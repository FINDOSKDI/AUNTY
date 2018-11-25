#!/usr/bin/env python
import sys
import pygraphviz as pgv
from metamodelo import *
with open(sys.argv[1], 'r') as f:
    au = str(f.read())
G = pgv.AGraph(automata2dot(mm.model_from_str(au)))
#G.layout(prog="dot")
G.draw(sys.argv[2], prog="dot")
