class Node:

    def __init__(self,  data):

        self. data =  data
        self.left = None
        self.right = None

class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)
    


class BinaryTree():

    def __init__(self):
        self.root=None

    def  preOrder(self, root):
        output=[]
        output.append(root.data)
        if root.left :
            output += self.preOrder(root.left)

        if root.right:
            output += self.preOrder(root.right)


        return output

    def  inOrder(self,root):
        output=[]
        if root.left:

            output += self. inOrder(root.left)

        output.append(root. data)

        if root.right:

            output += self. inOrder(root.right)

        return output

    def  postOrder(self, root):
        output = []
        if root.left:

            output += self. inOrder(root.left)

        if root.right:

            output += self. inOrder(root.right)

        output.append(root. data)

        return output



    def breadthFirst(self,root):
        queue = Queue()
        queue.enqueue(self.root)
        list_of_items = []

        while queue.peek():
            front = queue.dequeue()
            list_of_items.append(front.data)

            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)

        return list_of_items




    def max(self):
        """
        This function gets the maximum value in the tree
        """
        if self.root== None:
            return "You Binary tree is empty"
        def checkMax(root):
            if root == None:
                return -1
            if checkMax(root.left) > root.data:
                root.data = checkMax(root.left)
            if checkMax(root.right) > root.data:
                root.data = checkMax(root.right)
            return root.data
        return checkMax(self.root)

class BTS(BinaryTree):

    def add(self, data):

        node = Node( data)
        if self.root == None:
            self.root = node
            return node. data
        else :
            current = self.root
            while current:
                if current. data >  data:
                    if current.right:
                        current = current.right
                    else:
                       current.right = node
                       return

                if current. data <  data:
                    if current.left:
                        current = current.left
                    else:
                       current.left = node
                       return




    def contains(self, data):
        if  data == self.root:
            return True

        else :
            current=self.root

            while current:
                if current.data >  data:
                    if current.right:
                        current = current.right
                    else:
                        return False

                if current.data <  data:
                    if current.left:
                        current = current.left
                    else:
                        return False
                if current.data ==  data:
                    return True

            return False

if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(1)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    print(tree.breadthFirst(tree.root))