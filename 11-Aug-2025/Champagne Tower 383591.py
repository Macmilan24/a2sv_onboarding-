# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(101)]
    
        dp[0][0] = float(poured)
        
        for i in range(query_row):
            for j in range(i + 1):
                overflow = max(0.0, dp[i][j] - 1.0)
                
                dp[i + 1][j] += overflow / 2.0
                dp[i + 1][j + 1] += overflow / 2.0
        
        return min(1.0, dp[query_row][query_glass])