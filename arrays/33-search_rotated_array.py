'''
leetcode 33 - search in rotated sorted array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k
(0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            # we're in the left sorted half
            if nums[middle] >= nums[left]:
                if nums[middle] > target and nums[left] <= target:
                    right = middle - 1
                else:
                    left = middle + 1
            # right sorted side
            else:
                if nums[middle] < target and nums[right] >= target:
                    left = middle + 1
                else:
                    right = middle - 1
                
        # target not found
        return -1
