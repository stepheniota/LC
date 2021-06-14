'''
leetcode 104 - maximum depth of binary tree
Given the root of a binary tree, return its MAX DEPTH
'''
# tags: trees

class TreeNode:
    '''Def for a binary tree node'''
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
       # idea: recursive search, base case when node is None then return cur_max

        def bfs(node: TreeNode, cur_max=0) -> int:
            if node is None:
                return cur_max
            return max(bfs(node.left, cur_max+1), bfs(node.right, cur_max+1))

        return bfs(root)

