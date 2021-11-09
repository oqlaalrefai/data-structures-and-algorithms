from code_challenges.ZipList.ziplist import *
# from code_challenges.linked_list.linked_list import *


import pytest


def test_zip():

    expected = 'head -> 2 -> 4 -> 3 -> 9 -> 1 -> 5 -> NULL'

    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.append(1)
    Linked_List_1.append(3)
    Linked_List_1.append(2)
    Linked_List_2.append(5)
    Linked_List_2.append(9)
    Linked_List_2.append(4)
    actual = zip_lists(Linked_List_1,Linked_List_2)

    assert expected == actual

def test_zip2():
    expected = 'head -> 1 -> 5 -> 3 -> 9 -> 2 -> 4 -> NULL'

    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.append(1)
    Linked_List_1.append(3)
    Linked_List_1.append(2)
    Linked_List_2.append(5)
    Linked_List_2.append(9)
    Linked_List_2.append(4)
    
    actual = Linked_List_1.zip_lists(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual

def test_linked_list_zipped_with_after():
    # Arrange
    expected = 'head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL'
    # Actual
    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()


    Linked_List_1.append(3)
    Linked_List_1.append(3.5)
    Linked_List_1.append(1)


    Linked_List_2.append(6)
    Linked_List_2.append(4)
    Linked_List_2.append(2)



    actual = zip_lists(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual