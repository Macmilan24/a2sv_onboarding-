# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()

        while left < right:
            less_sum = nums[left] + nums[right]

            if less_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        return count
        