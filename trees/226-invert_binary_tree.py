'''
leetcode 226 - invert a binary tree
'''
from trees import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # idea: swap child nodes, iterate down a level and repeat on children
        # base: node is None
        if not root:
            return root
        root.left, root.right = root.right, root.left
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root
