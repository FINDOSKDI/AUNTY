#!/usr/bin/env python
import sys
import pygraphviz as pgv

G = pgv.AGraph(sys.argv[1])
#G.layout(prog="dot")
G.draw(sys.argv[2], prog="dot")
