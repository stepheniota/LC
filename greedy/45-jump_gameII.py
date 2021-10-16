""" Leetcode 45 - Jump Game II

    You are given an integer array nums. 
    You are initially positioned at the array's first index,
    and each element in the array represents your maximum 
    jump length at that position.
    Return true if you can reach the last index, or false otherwise.
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        elle = r = 0
        
        while r < len(nums) - 1:
            frontier = 0
            for i in range(elle, r + 1):
                frontier = max(frontier, i + nums[i])
            elle, r = r + 1, frontier
            count += 1
        return count