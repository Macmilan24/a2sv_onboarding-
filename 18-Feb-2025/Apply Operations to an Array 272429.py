# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        zero_index = 0
        
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[i], nums[zero_index] = 0, nums[i]
                zero_index += 1
        
        return nums
        
        
