# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visible = set()

        for num in nums:
            if num in visible:
                return True
            visible.add(num)
        
        return False
        