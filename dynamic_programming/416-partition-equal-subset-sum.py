'''
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.
'''
# tags: dynamic programming

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass






if __name__ == '__main__':
    solution = Solution()
    nums = [1,5,11,5]
    ans = True
    print(f'The correct answer to input {nums} should be {ans}: {(solution.rob(nums))}')

    nums = [1,2,3,5]
    ans = False
    print(f'The correct answer to input {nums} should be {ans}: {(solution.rob(nums))}')