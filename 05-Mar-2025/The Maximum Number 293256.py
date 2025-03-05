# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        count = 1
        prev = nums[0]

        for i in range(len(nums)):

            if nums[i] != prev:
                count += 1
                prev = nums[i]
            
            if count == 3:
                return nums[i]
        
        return nums[0]

        
            
            
        