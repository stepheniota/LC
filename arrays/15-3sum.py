'''
leetcode 15 - 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        out = []
        nums.sort()

        # three ptrs, fix one and use sliding window to find other two
        # take advantage of sorted property
        # check for duplicates

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            elif i > len(nums) - 3:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[left] + nums[right] + a
                if three_sum  == 0:
                    out.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < len(nums) and nums[left] == nums[left - 1]):
                        left += 1
                    while (right > 0 and nums[right] == nums[right + 1]):
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return out
