# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = set()
        res = 0

        for right in range(len(s)):

            while s[right] in visited:
                visited.discard(s[left])
                left += 1
            
            visited.add(s[right])
            res = max(res, right - left + 1)
        
        return res
        

        