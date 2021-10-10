""" leetcode 416 - Partition equal subset sum

    Given a non-empty array nums containing only positive integers, 
    find if the array can be partitioned into two subsets such that 
    the sum of elements in both subsets is equal.
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """ knapsack problem with weight sum(nums) / 2
                pseudopolynomial space and time complexity
        """
        subset_sum = sum(nums) / 2
        if subset_sum % 1 != 0:
            return False
        else:
            subset_sum = int(subset_sum)

        opt = [[False] * (len(nums) + 1) for i in range(subset_sum + 1)]
        opt[0] = [True] * (len(nums) + 1)

        for i in range(1, subset_sum + 1):
            for j, n in enumerate(nums, start=1):
                if n <= i:
                    opt[i][j] = opt[i][j - 1] or opt[i - n][j - 1]
                else:
                    opt[i][j] = opt[i][j - 1]

        return opt[-1][-1]

