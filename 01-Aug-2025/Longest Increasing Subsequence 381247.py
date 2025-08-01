# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dp(i, prev):
            if i == n:
                return 0

            if memo[i][prev + 1] == -1:
                take = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp(i + 1, i )
                not_take = dp(i + 1, prev)
                memo[i][prev + 1] = max(take, not_take)

            return memo[i][prev + 1]
        
        return dp(0, -1)
