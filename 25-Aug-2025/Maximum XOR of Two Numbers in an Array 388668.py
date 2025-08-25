# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_ = 0
        mask = 0
        
        for bit in range(31, -1, -1):
            mask |= (1 << bit)
            prefixes = {num & mask for num in nums}
            
            candidate = max_ | (1 << bit)
            
            if any((candidate ^ p) in prefixes for p in prefixes):
                max_ = candidate
        
        return max_