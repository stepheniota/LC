'''
leetcode 198 - house robber

You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only constraint stopping you from robbing each 
of them is that adjacent houses have security system connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
# tags: dynamic programming

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let opt[i] be the optimal solution for robbing the first i houses in nums
        opt = [0 for i, _ in enumerate(nums)]

        # the recurrence relation opt[i] = max(opt[i-1], nums[i] + opt[i-2])
        for i, val in enumerate(nums):
            if i == 0:
                opt[i] = val
            elif i == 1:
                opt[i] = max(val, opt[i - 1])
            else:
                opt[i] = max(opt[i - 1], val + opt[i - 2] )

        return opt[len(nums) - 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    ans = 4 
    print(f'The correct answer to input {nums} should be {ans}: {(solution.rob(nums))}')

    nums = [2, 7, 9, 3, 1]
    ans = 12
    print(f'The correct answer to input {nums} should be {ans}: {(solution.rob(nums))}')

    nums = [1, 2]
    ans = 2
    print(f'The correct answer to input {nums} should be {ans}: {(solution.rob(nums))}')



