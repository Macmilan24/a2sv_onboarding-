# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        total_even = sum(nums[i] for i in range(0, n, 2))
        total_odd = sum(nums[i] for i in range(1, n, 2))
        
        res = 0
        left_even = 0
        left_odd = 0
        
        for i in range(n):
            if i % 2 == 0:
                total_even -= nums[i]
            else:
                total_odd -= nums[i]
            
            if left_even + total_odd == left_odd + total_even:
                res += 1
            
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return res