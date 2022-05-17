"""leetcode 1 - two sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                return [i, seen[val]]
            seen[target - val] = i

		# Only for typecheckers.
        return None
