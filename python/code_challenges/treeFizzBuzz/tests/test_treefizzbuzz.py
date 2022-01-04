from treefizzbuzz import __version__
from treefizzbuzz.fizzbuzz import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def empty_tree():

    return BinaryTree()

@pytest.fixture
def fizzy_tree():
    ## preparing data
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(7)
    tree.root.left.left = Node(15)

    return tree

def test_empty_tree(empty_tree):

    expected = None
    actual = fizz_buzz_tree(empty_tree)
    assert expected == actual.root
        
def test_fizz_buzz_filled_tree(fizzy_tree):

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.val == 'Fizz'
    assert new_tree.root.left.val == 'Buzz'
    assert new_tree.root.right.val == '7'
    assert new_tree.root.left.left.val == 'FizzBuzz'