from merge_sort import __version__
from merge_sort import Merge,Mergesort


def test_version():
    assert __version__ == '0.1.0'

def test_empty():
    a = []
    actual = 'empty array'
    expected  = Mergesort(a)
    assert expected == actual

def test_fullArray():
    a = [8,4,23,42,16,15]
    actual = [4,8,15,16,23,42]
    expected = Mergesort(a)
    assert expected == actual

def test_fullArray2():
    a = [8,4,23,42,16,18,15]
    actual = [4,8,15,16,18,23,42]
    expected = Mergesort(a)
    assert expected == actual

def test_oneEleArr():
    a = [1]
    actual = [1]
    expected = Mergesort(a)
    assert expected == actual
