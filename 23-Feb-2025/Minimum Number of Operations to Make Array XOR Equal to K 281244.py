# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for value in nums:
            total ^= value
            
        if total == k:
            return 0
            
        bits = total ^ k
        count = 0
        while bits:
            count += bits & 1
            bits >>= 1
            
        return count
        