""" leetcode 70 - climbing stairs

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """ let opt[i] be the number of ways to reach the ith step
                base: opt[0], opt[1] = 1, 1
                recursion relation: opt[i] = opt[i - 2] + opt[i - 1]
                let one be opt[i - 1], let two be opt[i - 1]
        """
        
        opt, one, two = 1, 1, 1
        
        for i in range(2, n + 1):
            opt = one + two
            two, one = opt, two
            
        return opt

if __name__ == '__main__':
    sol = Solution()
    n = 2
    ans = 2
    print(f'The correct answer to input {n} should be {ans}: {(sol.climbStairs(n))}') 

    n = 3
    ans = 3
    print(f'The correct answer to input {n} should be {ans}: {(sol.climbStairs(n))}') 

    n = 4
    ans = 5
    print(f'The correct answer to input {n} should be {ans}: {(sol.climbStairs(n))}') 