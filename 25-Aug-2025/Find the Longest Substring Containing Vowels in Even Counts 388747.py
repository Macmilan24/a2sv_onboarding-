# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_bits = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        
        first_seen = {0: -1}
        mask = 0
        longest = 0
        
        for i, ch in enumerate(s):
            if ch in vowel_bits:
                bit = vowel_bits[ch]
                mask ^= (1 << bit)
            
            if mask in first_seen:
                length = i - first_seen[mask]
                if length > longest:
                    longest = length
            else:
                first_seen[mask] = i
        
        return longest