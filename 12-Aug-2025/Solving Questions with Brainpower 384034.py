# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n-1, -1, -1):
            points, jump = questions[i]
            next_question = min(n, i + jump + 1)
            dp[i] = max(points + dp[next_question], dp[i+1])
        
        return dp[0]