# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = {} 
        max_sum = 0
        slow = 0
        cur_sum = 0

        for fast, num in enumerate(nums):
            while num in visited and visited[num] >= slow:
                cur_sum -= nums[slow]
                slow += 1
            
            cur_sum += num
            visited[num] = fast

            max_sum = max(max_sum, cur_sum)
        return max_sum
   