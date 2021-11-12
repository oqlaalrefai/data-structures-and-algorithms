from stack_and_queue.node import Node


class EmptyStack(Exception):
    pass


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
# S = Stack()
# S.push(4)
# S.push(40)
# print(S)
# print(S.peek())
# print(S.is_empty())
# S.pop()
# print(S.pop())
# print(S.pop())
