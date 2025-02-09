# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        left, right = 0,0

        while right < n:
            if abs(left - right) >= indexDifference and abs(nums[left] - nums[right]) >= valueDifference:
                return [left, right]
            right += 1
            if right == n and left < n - 1:
                left += 1
                right = left
        
        return [-1,-1]