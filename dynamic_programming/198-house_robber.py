""" leetcode 198 - house robber

    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint 
    stopping you from robbing each of them is that adjacent houses have 
    security system connected and it will automatically contact the police 
    if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, 
    determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        """ Let opt[i] be the max amount robbed for first ith houses
            Base: opt[0] = nums[0], opt[1] = max(nums[0], nums[1])
            Relation: opt[i] = max(opt[i - 1], opt[i - 2] + nums[i])
        """
        if len(nums) < 3:
            return max(nums)
        
        # let one be opt[i - 2] and two be opt[i - 1]
        one, two = nums[0], max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            opt = max(one + nums[i], two)
            one, two = two, opt
            
        return opt



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