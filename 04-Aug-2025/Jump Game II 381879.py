# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            min_jumps = float('inf')
            for jump in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dp(i + jump))
            memo[i] = min_jumps
            return min_jumps
        return dp(0)