# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        majority_length = n // 3
        element_count = Counter(nums)

        ans = []

        for key, value in element_count.items():
            if value > majority_length:
                ans.append(key)
        
        return ans


        

        
        