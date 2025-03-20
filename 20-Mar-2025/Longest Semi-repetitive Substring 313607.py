# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
            
        max_sub = 0
        left = 0
        pair = 0

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                pair += 1
            
            while pair > 1:
                if left < len(s) and s[left] == s[left + 1]:
                    pair -= 1
                left += 1
            
            max_sub = max(max_sub, right - left + 1)
        
        return max_sub
                
