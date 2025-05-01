# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        max_right = [0] * n
        max_num = 0

        for i in range(n - 1, -1, -1):
            max_num = max(max_num, nums[i])
            max_right[i] = max_num
        
        left = 0

        max_length = 0
        for right in range(n):
            while nums[left] > max_right[right]:
                left += 1
            
            max_length = max(max_length, right - left)
        
        return max_length
            


        