from tree import __version__


def test_version():
    assert __version__ == '0.1.0'

from tree.tree import BinaryTree, Node, BTS
import pytest

def test_singleNode():
    '''add root TEST'''
    expected = 'singleNode'
    tree=BinaryTree()
    tree.root=Node('singleNode')
    actual = tree.root.data
    assert actual == expected

def test_AddleftRight():
    '''left adn right add child test'''
    tree1=BTS()
    tree1.add("D")
    tree1.add("A")
    tree1.add("E")
    actual = tree1.contains("E")==True and tree1.contains("A")==True and tree1.contains("D")==True
    expected = True
    assert actual == expected 

def test_preOrder():
    '''preoredr TEST'''
    tree=BinaryTree()
    tree.root=Node('AC')
    tree.root.left=Node('BC')
    tree.root.right=Node('CC')
    tree.root.left.left=Node('DC')
    tree.root.left.right=Node('EC')
    tree.root.right.left=Node('FC')
    actual =  tree.preOrder(tree.root)
    expected =['AC', 'BC', 'DC', 'EC', 'CC', 'FC']
    assert actual == expected 

def test_inorder():
    '''preorder TEST'''
    tree=BinaryTree()
    tree.root=Node('Ac')
    tree.root.left=Node('Bc')
    tree.root.right=Node('Cc')
    tree.root.left.left=Node('Dc')
    tree.root.left.right=Node('Ec')
    tree.root.right.left=Node('Fc')
    actual = tree.inOrder(tree.root)
    expected = ['Dc', 'Bc', 'Ec', 'Ac', 'Fc', 'Cc']
    assert actual == expected

def test_postorder():
    '''postorder TEST'''
    tree=BinaryTree()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    actual = tree.postOrder(tree.root)
    expected = [4, 2, 5, 6, 3, 1]
    assert actual == expected