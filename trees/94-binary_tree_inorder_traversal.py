""" lc 94 - binary tree inorder traversal

Given the root of a binary tree, return the inorder traversal of its
node values.
"""
from typing import Optional, List
from trees import TreeNode

class SolutionRecursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        traversal = []

        if root.left:
            traversal.extend(self.inorderTraversal(root.left))

        traversal.append(root.val)

        if root.right:
            traversal.extend(self.inorderTraversal(root.right))

        return traversal

class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                traversal.append(curr.val)
                curr = curr.right
                
        return traversal
            
