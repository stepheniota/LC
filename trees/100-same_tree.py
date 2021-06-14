'''
leetcode 100 - same tree
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
'''
# tags: trees

from trees import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # idea: recursive dfs search
        # base case: one or both nodes are None i.e. previous nodes were actually leaves

        def dfs(p: TreeNode, q: TreeNode) -> bool:
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False

        return dfs(p, q)

