# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexMap = {}

        for i, n in enumerate(nums):
            indexMap[n] = i
        
        for num, changenum in operations:
            index = indexMap[num]
            nums[index] = changenum
            indexMap[changenum] = index
        
        return nums
