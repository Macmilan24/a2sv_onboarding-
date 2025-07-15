# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums) - 1, 1, -1):
            largest_side = sorted_nums[i]
            side1 = sorted_nums[i - 1]
            side2 = sorted_nums[i - 2]
            
            if side1 + side2 > largest_side:
                perimeter = side1 + side2 + largest_side
                return perimeter
        
        return 0