# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        memo = {}
        
        def dfs(i, t):
            if i == n:
                return 0
            if (i, t) in memo:
                return memo[(i, t)]
            
            skip = dfs(i + 1, t)
            
            take = satisfaction[i] * t + dfs(i + 1, t + 1)
            
            memo[(i, t)] = max(skip, take)
            return memo[(i, t)]
        
        return dfs(0, 1)