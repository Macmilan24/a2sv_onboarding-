# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        iso_map = {}

        for i in range(len(s)):
            if s[i] in iso_map.keys():
                if iso_map[s[i]] != t[i]:
                    return False
            elif t[i] in iso_map.values():
                return False
            
            iso_map[s[i]] = t[i]
        
        return True
        