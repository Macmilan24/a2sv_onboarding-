# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid == 0:
                if len(nums) == 1 or nums[0] > nums[1]:
                    return 0
                else:
                    left = mid + 1
                    continue
            
            if mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
                    continue
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
