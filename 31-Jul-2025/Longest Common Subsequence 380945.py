# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            key = (i, j)

            if key in memo:
                return memo[key]

            if text1[i] == text2[j]:
                memo[key] = 1 + dp(i + 1, j + 1)
            else:
                memo[key] = max(dp(i + 1, j), dp(i, j + 1))

            return memo[key]

        return dp(0, 0)