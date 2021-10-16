""" Leetcode 230 - kth Smallest Element in a BST

    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values 
    of the nodes in the tree.
"""
from typing import Optional
from trees import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = []
        
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            tree.append(node.val)
            
        dfs(root)
        tree.sort()
        return tree[k-1]
        