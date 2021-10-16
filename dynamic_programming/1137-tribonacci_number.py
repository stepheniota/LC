""" leetcode 1137 - Nth Tribonacci number
    The Tribonacci sequence is defined as follows:
    T(n) = T(n - 1) + T(n - 2) + T(n - 3)
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        """ Idea: Iterative, cache prev 3 results. """

        # Base cases
        if n == 0: return 0
        elif n < 3: return 1
        
        one, two, three = 0, 1, 1
        for i in range(3, n + 1):
            opt = one + two + three
            one, two, three = two, three, opt  # cache last 3 answers
        
        return opt