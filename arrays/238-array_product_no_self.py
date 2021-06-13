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
# tags: arrays
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # opt[i] = prefix[i] * postfix[i]
        # prefix[i] = prefix[i - 2] * nums[i - 1]; base prefix[0] = 1
        # postfix[i]  = postfix[i + 2] * nums[i + 1]
        # opt[i] = prefix[i - 2] * nums[i - 1] * postfix[i + 2] * nums[i + 1]
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        opt = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i, vals in enumerate(zip(prefix, postfix)):
            opt[i] = vals[0] * vals[1]
        
        return opt


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 4]
    smun = [4, 3, 2, 1]
    ans = [24, 12, 8, 6]
    print(f'Input {nums} should return {ans}: {sol.productExceptSelf(nums)}')

    nums = [-1, 1, 0, -3, 3]
    ans = [0, 0, 9, 0, 0]
    print(f'Input {nums} should return {ans}: {sol.productExceptSelf(nums)}')


