# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        min_diff = float('inf')
        result = 0
        
        for i in range(n-1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            left_avg = left_sum // (i + 1)
            right_avg = right_sum // (n - i - 1)
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                result = i
        
        last_diff = total_sum // n
        if last_diff < min_diff:
            result = n - 1
            
        return result