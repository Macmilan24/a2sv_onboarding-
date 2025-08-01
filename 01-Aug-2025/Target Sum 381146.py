# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, cur_res):
            if i == n:
                if cur_res == target:
                    return 1
                else:
                    return 0
                    
            key = (i, cur_res)
            if key in memo:
                return memo[key]
            
            memo[key] = dp(i + 1, cur_res + nums[i]) + dp(i + 1, cur_res - nums[i])
            return memo[key]
        
        return dp(0,0)