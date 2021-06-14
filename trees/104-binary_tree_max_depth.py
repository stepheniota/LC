'''
leetcode 104 - maximum depth of binary tree
Given the root of a binary tree, return its MAX DEPTH
'''
# tags: trees

from trees import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
       # idea: recursive search, base case when node is None then return cur_max

        def dfs(node: TreeNode, cur_max=0) -> int:
            if node is None:
                return cur_max
            return max(bfs(node.left, cur_max+1), bfs(node.right, cur_max+1))

        return bfs(root)

