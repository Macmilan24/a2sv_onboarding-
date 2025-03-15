# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s_pos = 0  
        for char in t:
            if char == s[s_pos]:
                s_pos += 1  
                if s_pos == len(s):  
                    return True
        
        return False