""" leetcode 561 - array partition I

Given an integer array nums of 2n integers, 
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. 
Return the maximized sum.
"""
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        for i in range(0, len(nums) - 1, 2):
            ans += min(nums[i], nums[i+1])
        
        return ans

