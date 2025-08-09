# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2

        memo = defaultdict(tuple)

        def dp(n, cur_sum):
            if cur_sum == target:
                return True
            if n == len(nums) or cur_sum > target:
                return False
            
            state = (n, cur_sum)
            if state not in memo:
                memo[state] =  dp(n + 1, cur_sum + nums[n]) or dp(n + 1, cur_sum)
            
            return memo[state]
        
        return dp(0,0)
