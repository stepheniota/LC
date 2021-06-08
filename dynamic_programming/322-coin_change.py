'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''

# tags: dynamic programming

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt = [amount + 1] * (amount + 1)
        opt[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - c >= 0:
                    opt[i] = min(opt[i], 1 + opt[i - c])

        return opt[amount] if opt[amount] != amount + 1 else -1


if __name__ == '__main__':
    sol = Solution()

    coins = [1,2,5]
    amount = 11
    ans = 3

    print(sol.coinChange(coins, amount) == ans)