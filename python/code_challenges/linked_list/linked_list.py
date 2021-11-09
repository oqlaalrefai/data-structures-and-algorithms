


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

        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            return "item not in the list"
        else:
            new_node = Node(newdata)
            new_node.next = n.next
            n.next = new_node


    def insertBefore(self, x,newdata):
        if self.head is None:
            return "List has no element"


        if x == self.head.data:
            new_node = Node(newdata)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            return "item not in the list"
        else:
            new_node = Node(newdata)
            new_node.next = n.next
            n.next = new_node

            
    def kth(self,k):
        a = {}
        current = self.head
        counter = -1
        if k <0 :
            return "its negative value"
        
        while current != None :
            counter +=1
            current = current.next
        current = self.head
        if k > counter+1:
            return "the value is greater than number of nodes"
        while current != None:
            a[counter] = current.data
            counter -= 1
            current = current.next
        return a[k]
    def zipLists(self,list1, list2):
        if list1.head == None and list2.head == None:
            return 'the two lists is empty'
        if list2.head == None or list1.head == None:
            if list1.head == None :
                return list2
            if list2.head == None :
                return list1
        curr1 = list1.head
        curr2 = list2.head

        while curr2 and curr1:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
            if curr1.next == None:
                break
        if curr2:
            curr1.next = curr2
        return list1
class Node() :
    '''this class to create node'''
    def __init__(self,data) : # its a constructor
        self.data = data
        self.next = None


l = LinkedList()
l2 = LinkedList()
l2.append(11)
l2.append(12)
l.append(6)
l.append(1.67)
l.append(8)
l3 =LinkedList()

print(l3.zipLists(l2,l))