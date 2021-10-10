""" Leetcode 55 - Jump Game

    You are given an integer array nums. 
    You are initially positioned at the array's first index,
     and each element in the array represents your maximum 
     jump length at that position.
    Return true if you can reach the last index, or false otherwise.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        goal = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0