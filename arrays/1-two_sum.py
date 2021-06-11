'''
leetcode 1 - two sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
'''
# tags: arrays

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[val] = i



def test():
    sol = Solution()

    nums = [2,7,11,15]
    target = 9
    ans = [0,1]
    print(f'Test array 1: target {target} should yield {ans}')
    print(f'Answer: {sol.twoSum(nums, target)}')

    nums = [3,2,4]
    target = 6
    ans = [1,2]
    print(f'Test array 1: target {target} should yield {ans}')
    print(f'Answer: {sol.twoSum(nums, target)}')

    nums = [3,3]
    target = 6
    ans = [0,1]
    print(f'Test array 1: target {target} should yield {ans}')
    print(f'Answer: {sol.twoSum(nums, target)}')


if __name__ == '__main__':
    test()