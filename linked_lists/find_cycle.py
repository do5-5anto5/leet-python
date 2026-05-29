from node import Node
from doubly_linked import  DoublyLinkedList

def find_cycle(head: Node):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

dll = DoublyLinkedList()

dll.add_to_front(3)
dll.add_to_front(2)
dll.add_to_front(1)
dll.add_to_end(4)
dll.add_to_end(5)

# create the cycle appointing from last node to middle node
dll.tail.next = dll.head.next.next

print(find_cycle(dll.head))