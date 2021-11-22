from tree import __version__


def test_version():
    assert __version__ == '0.1.0'

from tree.tree import BinaryTree, Node, BTS,Queue
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


def test_maxExpectedoutcome(Test):
    '''test if its return the truely max value'''
    Expected = 6
    Actual = Test.max()
    assert Actual == Expected

def test_RaiseError(TEST):
    '''test if its raise error'''
    Expected = 'You Binary tree is empty'
    Actual = TEST.max()
    assert Actual == Expected




@pytest.fixture

def Test():
    tree = BinaryTree()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node5=Node(5)
    node6=Node(6)

    node1.left = node2
    node1.right = node3
    node3.left=node6
    node2.right = node5
    tree.root=node1


    return tree

def test_breadthFirst():
    tree2=BinaryTree()
    tree2.root=Node(1)
    tree2.root.left=Node(2)
    tree2.root.right=Node(3)
    tree2.root.left.left=Node(4)
    tree2.root.left.right=Node(5)
    tree2.root.right.left=Node(6)
    assert tree2.breadthFirst(tree2.root)==[1, 2, 3, 4, 5, 6]


def test_breadthFirst2():
    tree = BinaryTree()
    a_node = Node("A")
    b_node = Node("B")
    c_node = Node("C")
    d_node = Node("D")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["A", "B", "C", "D"]
    actual = tree.breadthFirst(tree.root)
    assert actual == expected

@pytest.fixture
def TEST():
    tree2 = BinaryTree()
    return tree2

