"""
the node is a piece of a Linked List (each node appointing to next node),
or a Doubly Linked List (each node appointing next and previous node)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None