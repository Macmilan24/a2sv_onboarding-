# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
            
        memo = [-1] * n 
        memo[0] = 0
        memo[1] = 1 

        def dp(n):
            if n <= 1:
                return n
            
            if memo[n - 1] == -1:
                memo[n - 1] = dp(n - 1) + dp(n - 2)
            
            return memo[n - 1]
        
        return dp(n)
            
        