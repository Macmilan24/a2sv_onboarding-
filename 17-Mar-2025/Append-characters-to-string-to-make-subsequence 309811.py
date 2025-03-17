# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first_ptr = 0
        second_ptr = 0

        while first_ptr < len(s) and second_ptr < len(t):
            if s[first_ptr] == t[second_ptr]:
                second_ptr += 1
            first_ptr += 1
        
        return len(t) - second_ptr