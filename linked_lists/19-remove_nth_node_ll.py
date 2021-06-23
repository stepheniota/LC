'''
leetcode 19 - remove nth node from end of list
Given the head of a linked list, remove the nth node 
from the end of the list and return its head.
'''
from linked_list import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''O(n) time complexity, O(1) space
           Idea: two pointers, offset by n. When dummy ptr reaches
           end of list, curr.next ptr points at node we need to remove
        '''
        
        # edge case of sz = 1
        if not head.next: 
            return None
        
        dummy = ListNode(next=head)
        curr = dummy
        while n >= 0:
            dummy = dummy.next
            n -= 1
            
        while dummy:
            curr = curr.next
            dummy = dummy.next
        
        # edge case that n == sz of linked list
        if curr.next == head:
            return curr.next.next
        
        # curr.next is now node that needs to be removed
        curr.next = curr.next.next
        
        return head
