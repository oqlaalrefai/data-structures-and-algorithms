from code_challenges.linked_list.linked_list import LinkedList,Node
from code_challenges.linked_list import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'
    
def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


def test_append_3_values(ll):
    expected = 'head -> 5 -> hello -> 1.67 -> NULL'
    actual = ll.__str__()
    assert expected == actual


def test_append_to_existing_ll(ll):
    ll.append(True)
    expected = 'head -> 5 -> hello -> 1.67 -> True -> NULL'
    actual = ll.__str__()
    assert expected == actual




def test_appendLast(ll):
    ll.append(25)
    expected = "head -> 5 -> hello -> 1.67 -> 25 -> NULL"
    actual = ll.__str__()
    assert expected == actual
def test_multi_values_to_end(ll):
    ll.append(25)
    ll.append(20)
    expected = "head -> 5 -> hello -> 1.67 -> 25 -> 20 -> NULL"
    actual = ll.__str__()
    assert expected == actual

def test_insert_a_node_before(ll):
    ll.insertBefore("hello",55)
    expected = "head -> 5 -> 55 -> hello -> 1.67 -> NULL"
    actual = ll.__str__()
    assert expected == actual
def test_insert_a_node_after(ll):
    ll.insertAfter("hello",100)
    expected = "head -> 5 -> hello -> 100 -> 1.67 -> NULL"
    actual = ll.__str__()
    assert expected == actual
def test_node_before_the_first_node(ll):
    ll.insertBefore(5,75)
    expected = "head -> 75 -> 5 -> hello -> 1.67 -> NULL"
    actual = ll.__str__()
    assert expected == actual
def test_after_the_last_node(ll):
    ll.insertAfter(1.67,200)
    expected = "head -> 5 -> hello -> 1.67 -> 200 -> NULL"
    actual = ll.__str__()
    assert expected == actual

def test_kGreater():

    expected = "the value is greater than number of nodes"
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth(5)
    assert actual == expected


def test_negative():

    expected = "its negative value"
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth(-1)
    assert actual == expected
    
def test_same_length():
    expected = 1
    ll = LinkedList()
    ll.append(1)
    ll.append(11)
    ll.append(14)
    actual = ll.kth(2)
    assert actual == expected

def test_size1():

    expected = 1
    ll = LinkedList()
    ll.append(1)
    actual = ll.kth(0)
    assert actual == expected

def test_kthMiddle():
    expected = 2
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    actual = ll.kth(2)
    assert actual == expected

def test_kthMiddle():
    expected = 1
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth(2)
    assert actual == expected



@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append('hello')
    ll.append(1.67)
    return ll
