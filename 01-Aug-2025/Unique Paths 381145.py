# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(row, col):
            if row == m or col == n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            key = (row, col)

            if key in memo:
                return memo[key]
            
            memo[key] = dp(row + 1, col) + dp(row, col + 1)
            return memo[key]
        
        return dp(0,0)
            

