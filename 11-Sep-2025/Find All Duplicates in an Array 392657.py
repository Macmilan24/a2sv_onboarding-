# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        duplicateMap = {}

        ans = []

        for num in nums:
            if num in duplicateMap:
                ans.append(num)
                duplicateMap[num] += 1
            else:
                duplicateMap[num] = 1
        
        return ans
        