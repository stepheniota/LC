""" Leetcode 55 - Jump Game

    You are given an integer array nums. 
    You are initially positioned at the array's first index,
     and each element in the array represents your maximum 
     jump length at that position.
    Return true if you can reach the last index, or false otherwise.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ Greedy solution:
                Initially, let the goal position be last index of nums
                Iterating in reverse, if you can reach to goal position
                from index i, update goal position to index i
            Return True if goal position is 0 after considering all nums
        """
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0