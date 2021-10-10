""" leetcode 300 - Longest increasing subsequence

    Given an integer array nums, return the length of the longest 
    strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array 
    by deleting some or no elements without changing the order of 
    the remaining elements. 
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        opt = [1] * n

        # let opt[i] denote the optimal subseq of length i
        # if we STARTED by including nums[i]
        # opt[i] = max_j(1 + opt[j]) for all i < j < n
        # ans is the max value in opt; ans = max(opt)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    opt[i] = max(opt[i], 1 + opt[j])

        return max(opt)

