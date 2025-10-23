# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        elm_count = Counter(nums)
        res = []
        req = len(nums)/3

        for elm, count in elm_count.items():
            if count > req:
                res.append(elm)
        
        return res