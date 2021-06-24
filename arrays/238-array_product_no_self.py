'''
leetcode 238 - Product of array except self

Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all
the elements of nums except nums[i].
The product of any prefix or suffix of nums is
guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time 
and without using the division operation.
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # idea: ans[i] = prefix[i] * suffix[i]
        # two passes to calculate each
        ans = [1] * n
        
        # calculate prefix for each nums[i]
        curr = nums[0]
        for i in range(1, n):
            ans[i] = curr
            curr *= nums[i]
        
        # calculate suffix for each num, and multiply by prefix
        curr = nums[-1]
        for i in range(n - 2, -1 , -1):
            ans[i] *= curr
            curr *= nums[i]
            
        return ans

if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 4]
    smun = [4, 3, 2, 1]
    ans = [24, 12, 8, 6]
    print(f'Input {nums} should return {ans}: {sol.productExceptSelf(nums)}')

    nums = [-1, 1, 0, -3, 3]
    ans = [0, 0, 9, 0, 0]
    print(f'Input {nums} should return {ans}: {sol.productExceptSelf(nums)}')


