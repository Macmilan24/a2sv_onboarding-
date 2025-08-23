# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for x in nums:
            xor_all ^= x  
        mask = xor_all & -xor_all   

        x = 0
        y = 0
        for num in nums:
            if num & mask:
                x ^= num  
            else:
                y ^= num   

        return [x, y]