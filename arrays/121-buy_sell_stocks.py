""" leetcode 121 - Best Time to Buy and Sell Stock

You are given an array prices where prices[i] 
is the price of a given stock on the ith day.
You want to maximize your profit by choosing a 
single day to buy one stock and choosing 
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        
        for p in prices:
            buy_price = min(buy_price, p)
            max_profit = max(max_profit, p - buy_price)
        
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    ans = 5
    print(f'The correct answer to input {prices} should be {ans}: {(sol.maxProfit(prices))}') 

    prices = [1,2]
    ans = 1
    print(f'The correct answer to input {prices} should be {ans}: {(sol.maxProfit(prices))}') 
