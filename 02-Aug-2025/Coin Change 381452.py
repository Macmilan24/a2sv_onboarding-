# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0: 
                return 0
            if rem < 0: 
                return float('inf')
            if rem in memo: 
                return memo[rem]
            memo[rem] = min(1 + dp(rem - coin) for coin in coins)
            
            return memo[rem]
        res = dp(amount)
        return res if res != float('inf') else -1