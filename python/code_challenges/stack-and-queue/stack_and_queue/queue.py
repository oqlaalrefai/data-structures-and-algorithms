from stack_and_queue.node import Node


class Queue:
    """
    a class that implements the Queue Data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    
    def enqueue(self, value):
        node=Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def __str__(self):
        retStr = ""

        current = self.front
        while(current != None):
            retStr += f" {current.data} <-"
            current = current.next
        return f'{retStr} rear '


    def dequeue(self):
        if self.front == None:
            return 'queue is empty'
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None
        return temp.data
    
    def peek(self):
        if self.front == None:
            return 'queue is empty'
        else :
            return self.front.data

    def is_empty(self):
        return self.front == None

# q = Queue()
# q.enqueue(1)
# q.enqueue(11)
# q.enqueue(10)
# print(q)
# q.dequeue()
# print(q)
# print(q.peek())
# print(q.is_empty())
