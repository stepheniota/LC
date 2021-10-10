""" leetcode 167 - Two sum II

    Given an array of integers numbers that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number.
    Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
    where 1 <= answer[0] < answer[1] <= numbers.length.
    The tests are generated such that there is exactly one solution. 
    You may not use the same element twice.
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        # idea: left and right point to smallest, largest element resp.
        # take L+R and compare to target. tune value by incrementing pointers 

        while left < right:
            two_sum = numbers[left] + numbers[right]
            if target == two_sum:
                return [left + 1, right + 1]
            elif target < two_sum:
                right -= 1
            else:
                left += 1

        # if a solution wasn't guaranteed
        return []

