# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        
        diff = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        
        
        if not diff:
            return True
        
        
        if len(diff) != 2:
            return False

        return diff[0][1] == diff[1][2] and diff[0][2] == diff[1][1]
        