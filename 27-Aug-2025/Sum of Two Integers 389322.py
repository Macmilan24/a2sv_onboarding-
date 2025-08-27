# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            s = (a ^ b) & MASK
            b = ((a & b) << 1) & MASK
            a = s
        
        return a if a <= MAX_INT else ~(a ^ MASK)