# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s, O_count, C_count):
            if len(s) == 2 * n:
                res.append(s)
                return
            if O_count < n:
                helper(s + '(', O_count + 1, C_count)
            if C_count < O_count:
                helper(s + ')', O_count , C_count + 1)
        
        helper('',0,0)
        
        return res
