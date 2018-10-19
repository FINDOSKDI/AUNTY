#!/usr/bin/env python
import sys
import pygraphviz as pgv
str=""" digraph {
A -> B
}"""
G = pgv.AGraph(str)
G.layout(prog='dot')
G.draw("tmp/aa.png", prog="dot")
