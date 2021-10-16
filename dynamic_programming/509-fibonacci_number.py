""" leetcode 509 - fibonacci number
	Given n, calculate Fib(n).
"""
class Solution:
    def fib(self, n: int) -> int:
        """ Idea: iterative, cache last 2 results
            Let opt denote ans to fib(i)
            base: fib(0) = 0, fib(1) = 1
            relation: opt = one + two
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        one, two = 0, 1
        for _ in range(2, n + 1):
            opt = one + two
            one, two = two, opt  # update cache for next iteration
        return opt