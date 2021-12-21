from depthfirst import __version__
from depthfirst.graph import *

def test_version():
    assert __version__ == '0.1.0'

def test_breadthFirst():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(d, f)

    assert graph.breadthFirst(a) == [a,b,c,d,e,f]