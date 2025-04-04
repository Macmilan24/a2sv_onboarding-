# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - left_sum

            if right_sum == left_sum:
                return i
            
            left_sum += nums[i]
        
        return -1
        