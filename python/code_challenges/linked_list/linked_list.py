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

        

        return f'{retStr} None'
    
    
    
    def includes(self,val): 
        # Initialize current to head
        current = self.head
 
        # loop till current not equal to None
        while current != None:
            if current.data == val:
                return f'{True} yes node is exist' # data found
            current = current.next
         
        return f'{False} node not found ' # Data Not found



class Node() :
    '''this class to create node'''
    def __init__(self,data) : # its a constructor
        self.data = data
        self.next = None



print(Node(5)) #it will create a node but it will print a addres value 

LL = LinkedList() #create instance from class
LL.append(3) 
LL.append(4)
LL.append(5)

print(LL.__str__())
