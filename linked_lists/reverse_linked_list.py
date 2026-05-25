"""
solved problem 'Reverse Linked List' from LeetCode
https://leetcode.com/problems/reverse-linked-list/
"""
class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Solution(object):
    def __init__(self, head):
        new_list = None
        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node