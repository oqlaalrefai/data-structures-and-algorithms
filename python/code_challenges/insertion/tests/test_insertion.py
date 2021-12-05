from insertion import __version__
from insertion.insertion.py import InsertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_emptyList():
    a = []
    actual = 'empty list'
    expected = InsertionSort(a)
    assert actual == expected

def test_emptyList():
    a = [8,4,23,42,16,15]
    actual = [4, 8, 15, 16, 23, 42]
    expected = InsertionSort(a)
    assert actual == expected

def test_emptyList():
    a = [8]
    actual = [8]
    expected = InsertionSort(a)
    assert actual == expected