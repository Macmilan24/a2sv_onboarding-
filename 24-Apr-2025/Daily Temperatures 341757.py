# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                temp, temp_idx = stack.pop()
                res[temp_idx] = i - temp_idx
            
            stack.append([temperatures[i], i])
        
        return res

        