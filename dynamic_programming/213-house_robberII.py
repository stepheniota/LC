""" Leetcode 213 - House Robber II

    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed. 
    All houses at this place are arranged in a circle. 
    That means the first house is the neighbor of the last one. 
    Meanwhile, adjacent houses have a security system connected, 
    and it will automatically contact the police if two adjacent houses
    were broken into on the same night.

    Given an integer array nums representing the amount of money 
    of each house, return the maximum amount of money you can rob
    tonight without alerting the police.
"""
from typing import List

class Solution:
    """ Run the House Robber I algorithm twice. 
        Once including the first house and excluding the last house,
        and another time excluding first house and including last house.
        Return the max between the two options.
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4: return max(nums)
        
        def loot(nums):
            if len(nums) < 3: return max(nums)
            
            one, two = nums[0], max(nums[1], nums[0])
            for i in range(2, len(nums)):
                opt = max(one + nums[i], two)
                one, two = two, opt
                
            return opt
            
        return max(loot(nums[:-1]), loot(nums[1:]))