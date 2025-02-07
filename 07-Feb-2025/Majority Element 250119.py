# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        
        return nums[len(nums) // 2]
        