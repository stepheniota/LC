
from trees import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
		# idea: swap child nodes, iterate down a level and repeat on children
		# base: node is None
        def invert(head: TreeNode) -> bool:
            if head == None:
                return True
            head.left, head.right = head.right, head.left
            invert(head.left), invert(head.right)

        invert(root)

        return root
