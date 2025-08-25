# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == n:
                return [[]]
            
            rest = dp(i + 1)
            
            with_curr = []
            for subset in rest:
                with_curr.append(subset + [nums[i]])
            
            memo[i] = rest + with_curr
            return memo[i]
        
        return dp(0)