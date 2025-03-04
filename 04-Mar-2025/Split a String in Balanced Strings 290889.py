# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        l_r_count = 0

        for i in range(len(s)):
            if l_r_count == 0:
                ans += 1
            
            if s[i] == "L":
                l_r_count += 1
            else:
                l_r_count -= 1
        
        return ans