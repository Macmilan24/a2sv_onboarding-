# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i].isalnum():
                s_map[s[i]] = s_map.get(s[i], 1) + 1
            if t[i].isalnum():
                t_map[t[i]] = t_map.get(t[i], 1) + 1
        
        return s_map == t_map


        