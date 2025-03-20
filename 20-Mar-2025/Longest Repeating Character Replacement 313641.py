# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        str_map = {}
        left = 0
        max_count = 0
        window_len = 0
        max_len = 0

        for right in range(len(s)):
            
            str_map[s[right]] = str_map.get(s[right], 0) + 1
            max_count = max(max_count, str_map[s[right]])
            window_len = right - left + 1

            while window_len - max_count > k:
                str_map[s[left]] -= 1
                left += 1
                window_len = right - left + 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
            
