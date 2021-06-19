'''
leetcode 152 - maximum product subarray
Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.
'''
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        glob_max = float('-inf')
        cur_max, cur_min = 1, 1

        for val in nums:
            tmp = val * cur_max
            cur_max = max(val * cur_max, val * cur_min, val)
            cur_min = min(tmp, val * cur_min, val)
            glob_max = max(cur_max, glob_max)

        return glob_max
