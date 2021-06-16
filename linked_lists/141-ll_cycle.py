'''
leetcode 141 - linked list cycle
Given head, the head of a linked list, 
determine if the linked list has a cycle in it.
'''
from linked_list import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False 


