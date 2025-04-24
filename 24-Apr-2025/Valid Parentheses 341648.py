# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{',']': '['}

        for char in s:
            if char in pair:
                if stack and pair[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False

        
