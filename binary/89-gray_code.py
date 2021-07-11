'''
leetcode 89 - gray code
An n-bit gray code sequence is a sequence of 2n integers where:
    * Every integer is in the inclusive range [0, 2n - 1],
    * The first integer is 0,
    * An integer appears no more than once in the sequence,
    * The binary representation of every pair of adjacent integers differs by exactly one bit, and
    * The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
'''

from typing import List

class Solution:
        #def bin_to_gray(n: int) -> int:
        #    return n ^ (n >> 1)
        
        return [i ^ (i >> 1) for i in range(2**n)]
