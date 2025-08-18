# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        dp[n][0] = 0
        dp[n][1] = 0

        for i in range(n-1, -1, -1):
            sell = prices[i] + dp[i + 2][0] if i + 2 <= n else prices[i]

            cooldown = dp[i + 1][1]
            dp[i][1] = max(sell, cooldown)

            buy = -prices[i] + dp[i + 1][1]
            cooldown = dp[i + 1][0]
            dp[i][0] = max(buy, cooldown)
        
        return dp[0][0]
