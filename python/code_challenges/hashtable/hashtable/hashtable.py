class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'

class Hashtable:
    def __init__(self, size=1024):
        self.map = [None]*size
        self.size = size

    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size

    def add(self, key, value):
        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
            self.map[hashed_key].add([key , value])
            return
        
        if self.contains(key):
            current = self.map[hashed_key].head
            while current:
                if current.data[0] == key :
                    current.data[1] = value
                current = current.next
            return           
        
        else:
            self.map[hashed_key].add([key , value])
            return
        

        




    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if current.data[0] == key :
                    return current.data[1]
                current = current.next
            return 'this key not found'
        else:
            return 'this key not found'

    def contains(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if current.data[0] == key :
                    return True
                current = current.next
            return False
        else:
            return False


if __name__ == "__main__":
    my_hash = Hashtable()
    my_hash.add('hello',20)
    my_hash.add('helol',30)
    print(my_hash.get('hello'))