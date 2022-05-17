""" lc 169 - majority element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """ Boyer-Moore Voting Algorithm. """
        count = majority = 0
        
        for n in nums:
            if count == 0:
                majority = n
            count += 1 if majority == n else -1

        return majority
