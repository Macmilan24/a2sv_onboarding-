# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_count = defaultdict(int)  
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            num_count[nums[right]] += 1
            current_sum += nums[right]

            
            if right - left + 1 > k:
                num_count[nums[left]] -= 1
                current_sum -= nums[left]
                if num_count[nums[left]] == 0:
                    del num_count[nums[left]]
                left += 1

            if right - left + 1 == k and len(num_count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum