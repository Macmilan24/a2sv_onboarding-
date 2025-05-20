# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        res = []
        total_shift = 0

        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            shifted_char = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
            res.append(shifted_char)

        return ''.join(reversed(res))