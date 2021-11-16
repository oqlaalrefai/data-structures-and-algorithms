class Node:
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


    def pop(self):
        if self.top == None:
            return "This stack is empty"
        else :    
            temp =self.top
            self.top=self.top.next
            temp.next=None
            return temp.data        

    def is_empty(self):
        if self.top == None:
            return True
        else :
            return False






def validate_brackets(Str):
    stack = Stack()

    for char in Str:

        if char == '{' or char == '(' or char == '[':
            stack.push(char) 
        elif char == '}' or char == ')' or char == ']':
            #print('hi')
            if stack.is_empty==True:
                return False
            top_element = stack.pop()
            #print(top_element)

            if not matching(top_element, char):
                return False
 
    if stack.is_empty==False:
        return False
              
    return True

def matching(openBracket, closeBracket):
    if openBracket == '(' and closeBracket == ')':
        return True
    if openBracket == '[' and closeBracket == ']':
        return True
    if openBracket == '{' and closeBracket == '}':
        return True  
    return False


#print(validate_brackets("{()()}"))