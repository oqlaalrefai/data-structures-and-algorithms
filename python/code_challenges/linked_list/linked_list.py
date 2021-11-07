# from code_challenges.linked_list import Li


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
            current.next = newNode
        else:
            self.head = newNode
    


    def __str__(self):
        retStr = "head ->"

        current = self.head
        while(current != None):
            retStr += f" {current.data} ->"
            current = current.next

        

        return f'{retStr} NULL'
    
    
    
    def includes(self,val): 
        # Initialize current to head
        current = self.head
 
        # loop till current not equal to None
        while current != None:
            if current.data == val:
                return f'{True} yes node is exist' # data found
            current = current.next
         
        return f'{False} node not found ' # Data Not found


    def insertAfter(self, x, newdata):
        

        n = self.head
        print(n.next)
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(newdata)
            new_node.next = n.next
            n.next = new_node


    def insertBefore(self, x,newdata):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.data:
            new_node = Node(newdata)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        print(n.next)
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node = Node(newdata)
            new_node.next = n.next
            n.next = new_node
        
class Node() :
    '''this class to create node'''
    def __init__(self,data) : # its a constructor
        self.data = data
        self.next = None


l = LinkedList()
l.append(6)
l.append(1.67)
l.insertAfter(1.67,'yes')
l.insertBefore('yes','no')
print(l)