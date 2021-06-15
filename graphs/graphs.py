'''Node class as defined in leetcode problems'''

class Node:
    '''Def for a Node'''
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
