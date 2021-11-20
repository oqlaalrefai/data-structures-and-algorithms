class Node:

    def __init__(self,  data):

        self. data =  data
        self.left = None
        self.right = None



class BinaryTree:

    def __init__(self):
        self.root=None

    def  preOrder(self, root):
        output=[]
        output.append(root. data)
        if root.left :
            output += self. preOrder(root.left)

        if root.right:
            output += self. preOrder(root.right)


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
