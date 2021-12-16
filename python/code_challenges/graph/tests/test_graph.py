from graph import __version__
from graph.graph import Graph,Vertex,Edge
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_add_node(): ## test 1
    
    graph = Graph()

    expected = 'apple' 

    actual = graph.add_node('apple').value

    assert actual == expected

def test_add_edge_start():
    
    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)




def test_add_edge_end():
    
    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_other_case():
    
    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)


# def test_get_neighbors():

#     graph = Graph()

#     meat = graph.add_node('meat')
#     chicken = graph.add_node('chicken')

#     graph.add_edge(meat, chicken)

#     expected = ('chicken', 0)
#     actual = graph.get_neighbors(meat)
#     assert actual == expected

def test_get_nodes():

    graph = Graph()

    meat = graph.add_node('meat')

    chicken = graph.add_node('chicken')

    tomato = Vertex('tomato')

    expected = 2

    actual = len(graph.get_nodes())
    
    assert actual == expected



def test_size():

    graph = Graph()

    graph.add_node('osama')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_size_empty(): 

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected