# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        pre = 1
        for i in range(n):
            result[i] *= pre
            pre *= nums[i]
        
        post = 1

        for i in range(n - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        
        return result
