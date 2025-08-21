# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(remain):
            if remain == 0:
                return 1
            if remain in memo:
                return memo[remain]
            
            ways = 0
            for num in nums:
                if remain - num >= 0:
                    ways += dp(remain - num)
            
            memo[remain] = ways
            return ways
        
        return dp(target)