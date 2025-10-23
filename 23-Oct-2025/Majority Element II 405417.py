# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        elm_count = Counter(nums)
        res = []
        req = len(nums)/3

        for elm, count in elm_count.items():
            if count > req:
                res.append(elm)
        
        return res