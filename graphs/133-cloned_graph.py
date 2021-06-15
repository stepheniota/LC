'''
leetcode 133 - clone a graph
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
'''

from graphs import Node

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # idea: a visited node is a node that's been copied
        # store copied nodes in a dict keyed by their values
        # keys of nodes are distict, so this works
        visited = {}

        def clone_node(node):

            cloned_node = Node(val=node.val)
            visited[cloned_node.val] = cloned_node

            for nei in node.neighbors:

                if nei.val not in visited:
                    cloned_nei = clone_node(nei)
                else:
                    cloned_nei = visited[nei.val]
                cloned_node.neighbors.append(cloned_nei)
            return cloned_node

        return clone_node(node)
