# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        total_sum = sum(nums)
        if total_sum < x:
            return -1
        if total_sum == x:
            return len(nums)
        
        target = total_sum - x

        left = 0
        cur_sum = 0
        max_len = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
            
        if max_len == 0:
            return -1
        
        return len(nums) - max_len