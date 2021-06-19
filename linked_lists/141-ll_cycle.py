'''
leetcode 141 - linked list cycle
Given head, the head of a linked list, 
determine if the linked list has a cycle in it.
'''
from linked_list import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''hashset approach; O(n) time and space'''
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False 

    def hasCycle2(self, head: ListNode) -> bool:
        '''2 ptr approach; O(n) time, O(1) space'''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

    


