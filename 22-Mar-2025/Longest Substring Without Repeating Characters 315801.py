# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        ans = 0

        for right in range(len(s)):
            while s[right] in window:
                window.discard(s[left])
                left += 1
            
            window.add(s[right])

            ans = max(ans, right - left + 1)
        
        return ans

        