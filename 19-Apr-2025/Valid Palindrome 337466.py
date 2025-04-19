# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return new_s == new_s[::-1]
        