from typing import Counter


class LinkedList:
    '''this class will link each node together'''
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                if current.next == None :
                    current.next = newNode
        else:
            self.head = newNode
    def appendbefore(self,value,newVal):

        newnode = Node(newVal)
        current = self.head
        if current.data==None:
            return False
        while current != None:
            if current.next.data == value:
                newnode.next = current.next
                current.next.data = newnode.data
    
  

        

    
    



class Node() :
    '''this class to create node'''
    def __init__(self,data) : # its a constructor
        self.data = data
        self.next = None



ll = LinkedList()
ll.append(5)
ll.append('Hello')
ll.append(1.67)
print(ll)