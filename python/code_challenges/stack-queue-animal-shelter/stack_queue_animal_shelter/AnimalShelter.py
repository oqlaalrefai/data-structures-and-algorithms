class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Queue:
    """
    Class: Queue
    """

    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self,data):
        node = Node(data)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            return "can't dequeue an empty queue."
        elif self.front.next == None:
            temp_node = self.front
            self.front = None

            return temp_node.data
        else:
            temp_node = self.front
            self.front = self.front.next

            return temp_node.data

    def peek(self):
        if self.front != None:
            return self.front.data
        else:
            return "can't return the front of the queue"

    def is_empty(self):
        return not self.front

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self,animal):
        if animal.lower() == "cat":
            self.cats.enqueue("cat")
        elif animal.lower() == "dog":
            self.dogs.enqueue("cat")
        else:
            return "invalid input"

    def dequeue(self,pref):
        if not pref.lower()=="cat" and not pref.lower()== "dog":
            return None
        elif self.dogs.is_empty() and self.cats.is_empty():
            return "can't remove or return a data from empty animal shelter"
        elif pref.lower() == "cat" and not self.cats.is_empty():
            return self.cats.dequeue()
        elif pref.lower() == "dog" and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref.lower() == "cat" and self.cats.is_empty() and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref.lower() == "dog" and self.dogs.is_empty() and not self.cats.is_empty():
            return self.cats.dequeue()
        else:
            return None
