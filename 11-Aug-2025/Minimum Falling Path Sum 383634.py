# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) 
        
        if n == 1:
            return matrix[0][0]
        
        dp = [[0] * n for _ in range(n)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, n):
            for j in range(n):
                left = dp[i-1][j-1] if j-1 >= 0 else float('inf')
                middle = dp[i-1][j]

                right = dp[i-1][j+1] if j+1 < n else float('inf') 
                dp[i][j] = matrix[i][j] + min(left, middle, right)
        
        return min(dp[n-1])