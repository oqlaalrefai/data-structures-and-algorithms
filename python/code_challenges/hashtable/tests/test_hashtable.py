from hashtable import __version__
from hashtable.hashtable import Hashtable

# def test_version():
#     assert __version__ == '0.1.0'


def test_add():
    table = Hashtable()
    table.add('data','orange')
    assert table.map[table.hash('data')].head.data == ['data','orange']


def test_hash_get(): 
    ht = Hashtable()
    ht.add('dog','cat')
    actual = ht.get('dog')
    assert actual == 'cat'

def test_return_none(): 
    ht = Hashtable()
    ht.add('dog','ant')
    assert ht.contains('dog') == True
    assert ht.contains('cat') == False

def test_hash_handles_collisions(): ## test 4
    ht = Hashtable()
    ht.add('dog', 'ant')
    ht.add('god', 'camel')
    actual = ht.get('dog')
    actual = ht.get('god')
    assert actual == 'camel'

def test_hash(): ## test 6
    ht = Hashtable()
    hash_val = ht.hash('apple')
    assert ht.hash('apple') == hash_val