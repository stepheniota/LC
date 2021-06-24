'''
leetcode 24 - swap nodes in pairs
Given a linked list, swap every two adjacent nodes and return its head. 
'''

from linked_list import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        tail, curr = dummy, head
        
        while curr and curr.next:
            prev = curr.next  # ptr to be swapped in front of curr
            future = curr.next.next  # node to be swapped next iter
            
            prev.next = curr
            curr.next = future
            tail.next = prev  # also updates dummy.next during first iter
        
            curr, tail = future, curr  # update ptrs for next iter
            
        return dummy.next
