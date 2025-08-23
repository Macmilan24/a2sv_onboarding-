# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        memo = {}  
        
        def dp(steps, r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0

            if steps == 0:
                return 1.0
            key = (steps, r, c)
            if key in memo:
                return memo[key]
            
            prob = 0.0
            for dr, dc in moves:
                prob += dp(steps - 1, r + dr, c + dc) / 8.0
            
            memo[key] = prob
            return prob
        
        return dp(k, row, column)