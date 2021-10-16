""" Leetcode 740 - Delete and Earn

    You are given an integer array nums. You want to maximize the
    number of points you get by performing the following operation 
    any number of times:
        * Pick any nums[i] and delete it to earn nums[i] points. 
          Afterwards, you must delete every element equal 
          to nums[i] - 1 and every element equal to nums[i] + 1.

    Return the maximum number of points you can earn by applying 
    the above operation some number of times
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """ Create dict mapping unique values in nums to 
            the total points they bring.
            Then by iterating over dict keys in sorted order,
            this problem reduces typical DP problem.
            Can be further optimized to use less extra space.
        """

        # in lieu of collections.Counter
        counts = {}
        for i in nums:
            if i in counts: counts[i] += i
            else: counts[i] = i
                
        keys = sorted(counts.keys(), reverse=True)
        
        n = len(keys)
        if n == 1:
            return counts[keys[0]]
        
        opt = [0] * n
        opt[0] = counts[keys[0]]
        if keys[1] == keys[0] - 1:
            opt[1] = max(opt[0], counts[keys[1]])
        else:
            opt[1] = opt[0] + counts[keys[1]]
        
        for i in range(2, n):
            if keys[i] == keys[i - 1] - 1:
                opt[i] = max(opt[i - 1], opt[i - 2] + counts[keys[i]])
            else:
                opt[i] = opt[i - 1] + counts[keys[i]]
                
        return opt[-1]