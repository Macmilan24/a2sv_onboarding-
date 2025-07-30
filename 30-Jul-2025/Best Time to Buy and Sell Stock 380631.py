# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(l, r, maxProfit):
            if r == len(prices):
                return maxProfit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            return dp(l, r + 1, maxProfit)
        return dp(0, 1, 0)