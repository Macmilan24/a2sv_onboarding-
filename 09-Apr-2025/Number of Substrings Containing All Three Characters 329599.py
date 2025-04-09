# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0] * 3 
        total = 0
        left = 0
        n = len(s)
        
        for right in range(n):
            count[ord(s[right]) - ord('a')] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                total += n - right 
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
                
        return total