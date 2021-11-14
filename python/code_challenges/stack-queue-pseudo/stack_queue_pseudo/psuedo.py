class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    """
    a class that implements the Stack Data structure
    """
    def __init__(self):
        self.top=None
    
    def push(self, value):
        node = Node(value)
        if self.top:
            node.next=self.top

        self.top=node
    
    
    def __str__(self):
        retStr = ""

        current = self.top
        while(current != None):
            retStr += f" {current.data} <-"
            current = current.next
        return f'{retStr} '        

   
    def pop(self):

        if self.top == None:
            return "This stack is empty"
        else :    
            temp =self.top
            self.top=self.top.next
            temp.next=None
            return temp.data        



    def peek(self):
        if self.top == None:
            return "This stack is empty"
        else :
            return self.top.data

    def is_empty(self):
        if self.top == None:
            return True
        else :
            return False



class Psuedo:
    def __init__(self):
        self.firstStack = Stack()
        self.secondStack = Stack()
        self.count = 0
    

    def enqueue(self, data):
        self.firstStack.push(data)


    def dequeue(self):
        while not self.firstStack.is_empty() : 
            self.secondStack.push(self.firstStack.pop())

        if self.secondStack.is_empty ( ) :
            raise RuntimeError('cannot dequeue  from empty stack!!') 

        return self.secondStack.pop()