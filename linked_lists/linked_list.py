''' Base class for linked list, as defined by leet-code.'''

class ListNode:
    '''Singly-linked-list'''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ret = []
        while self.next:
           ret.append(self.val) 
        return str(ret)
