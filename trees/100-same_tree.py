'''
leetcode 100 - same tree
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
'''
# tags: trees

class TreeNode:
    ''' Def for a binary tree node'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def dfs(p: TreeNode, q: TreeNode) -> bool:
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False

        return dfs(p, q)

