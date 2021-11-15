from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.AnimalShelter import AnimalShelter

def test_version():
    assert __version__ == '0.1.0'

def test_shelter_happy_path():

    shelter = AnimalShelter()
    shelter.enqueue("CAT")
    shelter.enqueue("CAT")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    expected = "cat"

    actual = shelter.dequeue("cat")
    assert actual == expected

def test_expectedFailur():
    shelter = AnimalShelter()
    actual = print(shelter.enqueue("dog"))
    expected = None
    assert actual == expected

def test_expectedFailur2():

    shelter = AnimalShelter()
    shelter.enqueue("CAT")
    shelter.enqueue("CAT")
    shelter.dequeue('CAT')
    shelter.dequeue('CAT')
    actual = "can't remove or return a data from empty animal shelter"
    excepted = shelter.dequeue('CAT')
    assert actual == excepted


def test_EdgeCase():
    shelter = AnimalShelter()
    shelter.enqueue("CAT")
    expected = shelter.dequeue("CAT")
    actual = 'cat'
    assert expected == actual