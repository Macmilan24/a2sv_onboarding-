# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        stack = []

        for i, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                idx, m = stack.pop()
                left = idx - stack[-1][0] if stack else idx + 1
                right = i - idx
                res = (res + m * left * right) % mod
            stack.append((i, num))
        
        for i in range(len(stack)):
            idx, num = stack[i]
            left = idx - stack[i - 1][0] if i > 0 else idx + 1
            right = len(arr) - idx
            res = (res + num * left * right) % mod
        
        return res