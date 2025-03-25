# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum = {}

        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in two_sum:
                return [two_sum[diff], i]
            
            two_sum[nums[i]] = i
        