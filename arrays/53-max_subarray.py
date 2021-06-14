'''
leetcode 53 - maximun subarray

Given an integer array nums, find the contiguous subarray(containing at least one number)
which has the largest sum and return its sum.
'''
# tags: arrays
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # idea: if a contiguous block has a negative sum, throw it away
        max_sum = nums[0]
        cur_sum = 0

        for val in nums:
            cur_sum += val
            max_sum = max(cur_sum, max_sum)
            # throw away negative prefix, doesn't add any value
            if cur_sum < 0:
                cur_sum = 0
    
        return max_sum
            


if __name__ == '__main__':
    sol = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = 6
    print(f'Input {nums} should return {ans}: {sol.maxSubArray(nums)}')

    nums = [1]
    ans = 1
    print(f'Input {nums} should return {ans}: {sol.maxSubArray(nums)}')

    nums = [5, 4, -1, 7, 8]
    ans = 23
    print(f'Input {nums} should return {ans}: {sol.maxSubArray(nums)}')

    nums = [-1, -2, -1, -1, -3]
    ans = -1
    print(f'Input {nums} should return {ans}: {sol.maxSubArray(nums)}')
