'''
leetcode 217 - contains duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
# tags: arrays

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # store previously seen nums
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 1]
    ans = True
    print(f'Input {nums} should return {ans}: {sol.containsDuplicate(nums)}')
    
    nums = [1, 2, 3, 4]
    ans = False
    print(f'Input {nums} should return {ans}: {sol.containsDuplicate(nums)}')

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ans = True
    print(f'Input {nums} should return {ans}: {sol.containsDuplicate(nums)}')
