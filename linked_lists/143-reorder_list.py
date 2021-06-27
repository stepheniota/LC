'''
leetcode 143 - reorder list
You are given the head of a singly linked-list.
The list can be represented as:
     L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.
'''

from linked_list import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        dummy = ListNode()
        curr, last = dummy, head
        
        stack = []
        while last:
            stack.append(last)
            last = last.next
        
        while True:
            if curr == head:
                break
                
            curr.next = head
            head = head.next
            curr = curr.next
            
            if curr == stack[-1]:
                break
            
            curr.next = stack.pop()
            curr = curr.next
            
        curr.next = None
        return dummy.next

            
