# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub_str = ""
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()

                n = ""

                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                stack.append(int(n) * sub_str)
        
        return "".join(stack)