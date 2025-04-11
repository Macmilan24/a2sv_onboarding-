# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
            
        begin = 0
        longest = 1
        
        for spot in range(n + n - 1):
            a = (spot - 1) // 2
            b = spot // 2
            
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1
            
            chunk = b - a - 1
            if chunk > longest:
                longest = chunk
                begin = a + 1
        
        return s[begin:begin + longest]