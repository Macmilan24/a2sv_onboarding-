# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1
            
        required = len(target)
        formed = 0
        window = {}
        
        left = right = 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in target and window[char] == target[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                window[char] -= 1
                if char in target and window[char] < target[char]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return min_window