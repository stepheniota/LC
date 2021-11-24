""" leetcode 104 - maximum depth of binary tree

Given the root of a binary tree, return its maximum depth.
"""
from trees import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




