# Singly Linked List
create linked list with certain class method


## Challenge
- create linked list with certain class method :
  - to string
  - insert
  - includes

## Approach & Efficiency
I used class and loops to create methods related to linkedList data structure

## API
* Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.\
* Linked List
include a head property this class to link all nodes together
  - class methods :
    - insert : Adds a new node with that value to the head
    - includes : Indicates whether that value exists as a Node’s value somewhere within the list.
    - to string : Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"


- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list
