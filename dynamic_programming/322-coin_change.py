""" leetcode 322 - coin change

    You are given an integer array coins representing coins of different denominations 
    and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # let opt[i] be min num coins needed for amount i in range [0, amount]
        # opt[i] = min_{coin} (1 + opt[i - coin]) for all coin in coins if coin <= amount
        # otherwise default val amount + 1 if no solution
        opt = [amount + 1] * (amount + 1)
        opt[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    opt[i] = min(opt[i], 1 + opt[i - c])

        return opt[amount] if opt[amount] != amount + 1 else -1




if __name__ == '__main__':
    sol = Solution()

    coins = [1,2,5]
    amount = 11
    ans = 3

    print(sol.coinChange(coins, amount) == ans)
