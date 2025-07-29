# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(n):
            if n >= len(nums):
                return 0
            
            if n in memo:
                return memo[n]
            
            cur_rob = nums[n] + dp(n + 2)
            next_rob = dp(n + 1)
            memo[n] = max(cur_rob, next_rob)
            return memo[n]
        
        return dp(0)