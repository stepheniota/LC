""" leetcode 198 - rotate array
    Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n    # takes care of edge case k > n

        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]
        return 
