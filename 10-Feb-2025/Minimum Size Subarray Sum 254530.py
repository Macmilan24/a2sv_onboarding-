# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        sumOfCurrent = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrent += nums[right]

            while sumOfCurrent >= target:
                res = min(res, right - left + 1)
                sumOfCurrent -= nums[left]
                left += 1

        return res if res != float('inf') else 0 
        