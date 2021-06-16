'''
leetcode 206 - reverse a linked list
Given the head of a singly linked list, 
reverse the list, and return the reversed list.
'''
from linked_list import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp

        return last