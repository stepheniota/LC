'''
leetcode 338 - counting bits
Given an integer n, return an array ans of length n + 1 such that
for each i (0<=i<=n), ans[i] is the number of 1's in the binary representation of i.
'''
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
		# let opt[i] be solution for ith integer
		# opt[i] = 1 + opt[j] where j is the binary num where all bits
		# except first 1 are the same
        opt = [0] * (n + 1)

        count = 1
        max_count = 1

        for i in range(1, n + 1):
            if i == 1:
                opt[1] = 1
            else:
                opt[i] = 1 + opt[count - 1]

            count += 1
            if count > max_count:
                count = 1
                max_count = max_count*2

        return opt
