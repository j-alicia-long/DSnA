# Linked List

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

list1 = LinkedList()
list1.val = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.val.next = e2

# Link second Node to third node
e2.next = e3
