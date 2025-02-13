# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        slow = 0
        count = 0

        for fast in range(len(s)):
            if s[fast] == "0":  
                count += fast - slow    
                slow += 1               
        
        return count