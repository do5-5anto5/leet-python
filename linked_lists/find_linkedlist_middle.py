from node import Node

class DLLOddLength:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    # To solve this problem is simple:

    def find_middle(self):
        # Put two pointers at head Node
        ahead = self.head
        middle = self.head

        while ahead and ahead.next:
            # The ahead pointer 'walks' twice
            ahead = ahead.next.next
            # The middle pointer 'walks' once
            middle = middle.next

        # When the ahead pointer can't walk, the middle pointer that walked a half than it, is in the middle Node

        return middle.value

dll = DLLOddLength()

dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)

print(dll.find_middle())