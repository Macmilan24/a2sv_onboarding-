# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        list_sum = sum(nums[:k])
        max_sum = list_sum

        for i in range(k,len(nums)):
            list_sum = list_sum - nums[i - k] + nums[i]
            max_sum = max(list_sum, max_sum)
        
        return max_sum / k

             
        