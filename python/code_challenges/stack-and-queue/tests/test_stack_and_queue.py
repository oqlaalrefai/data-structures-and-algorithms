from stack_and_queue import __version__
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue
from stack_and_queue.node import Node

def test_version():
    assert __version__ == '0.1.0'

import pytest


def test_is_empty():
    """
    is_empty test
    """
    stack=Stack()
    expected=True
    actual= stack.is_empty()
    assert expected == actual

def test_push():
    """
    push method test
    """
    stack=Stack()
    stack.push(8)
    expected=8
    actual=stack.top.data

    assert expected == actual

def test_pushMulti():
    """
    push method test for pushing multi item in stack
    """
    stack=Stack()
    stack.push(18)
    stack.push(27)
    stack.push('pushed')
    expected='pushed'
    actual=stack.top.data

    assert expected == actual

def test_multiPops():
    """
    pop method test to empty the stack
    """
    stack=Stack()
    stack.push(10)
    stack.push('data')

    stack.pop()
    stack.pop()
    expected=True
    actual=stack.is_empty()
    assert actual==expected

def test_pop():
    """
     pop method test
    """
    stack=Stack()
    stack.push(7)
    stack.push(15)
    stack.push(26)
    expected=26
    actual=stack.pop()
    assert actual==expected
    
def test_peek():
    """
    peek method test
    """
    stack=Stack()
    stack.push(0)
    stack.push(21)
    stack.push(35)
    expected=35
    actual=stack.peek()
    assert expected==actual

def test_peek_empty_stack():
    '''test peek when the stack is empty'''
    stack=Stack()
    expected='This stack is empty'
    actual=stack.peek()
    assert expected==actual


#------------------------
# Queue Tests
#------------------------


def test_is_empty():
    """
      is_empty test
    """
    q=Queue()
    expected=True
    actual= q.is_empty()
    assert expected == actual

def test_enqueue():
    """
    enqueue method test
    """
    q=Queue()
    q.enqueue(14)
    expected=14
    actual=q.rear.data

    assert expected == actual


def test_enqueueMulti():
    """
    enqueue method test for multi node
    """
    q=Queue()
    q.enqueue(10)
    q.enqueue(5)
    q.enqueue(0)
    expected=0
    actual=q.rear.data

    assert expected == actual


def test_dequeue():
    """
    dequeue method test
    """
    q=Queue()
    q.enqueue(10)
    q.enqueue(12)
    q.enqueue(13)
    expected=10
    actual=q.dequeue()
    assert actual==expected

def test_dequeueData():
    """
    dequeue all data test
    """
    q=Queue()
    q.enqueue(10)
    q.enqueue(1)
    q.enqueue(7)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    expected=True
    actual=q.is_empty()
    assert actual==expected


def test_peek():
    '''peek test'''
    q=Queue()
    q.enqueue(99)
    q.enqueue(7)
    q.enqueue(19)
    expected=99
    actual=q.peek()
    assert expected==actual

def test_peek2():
    '''empty queue peek testing'''
    q=Queue()
    expected='queue is empty'
    actual=q.peek()
    assert expected==actual