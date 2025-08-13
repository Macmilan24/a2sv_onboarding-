# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        memo = [[-1] * n for _ in range(m)]
        
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            right = dp(i, j+1)
            down = dp(i+1, j)
            memo[i][j] = right + down
            
            return memo[i][j]
        
        return dp(0, 0)