# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        max_val = max(nums)
        ans = 0
        left = 0
        max_val_count = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == max_val:
                max_val_count += 1

            while max_val_count == k:
                ans += (n - right)

                if nums[left] == max_val:
                    max_val_count -= 1
                left += 1
        
        return ans