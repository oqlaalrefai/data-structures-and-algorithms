# hashTable
<!-- Short summary or background information -->
A HASH TABLE is a data structure that stores values using a pair of keys and values. Each value is assigned a unique key that is generated using a hash function.

The name of the key is used to access its associated value
## Challenge
<!-- Description of the challenge -->
mplement a Hashtable with the following methods:

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get: takes in the key and returns the value from the table.

contains: takes in the key and returns a boolean, indicating if the key exists in the table already.

hash: takes in an arbitrary key and returns an index in the collection.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
An array was the chosen data structure to use for the HashTable and a linked list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

time -> O(1)
space -> O(1)

## API
<!-- Description of each method publicly available in each of your hashtable -->
- hash : to map general keys to corresponding indices in a table
- get : it will take a key and it will return a Value associated with that key in the table
- contains: Takes in the key and returns a boolean, indicating if the key exists in the table already.
- add : first it will hash the key, and then add the key and value pair to the table and it will handle the collisions if its happened
