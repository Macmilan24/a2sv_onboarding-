# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        sum_map = {0: - 1}
        cont_sum = 0

        if k <= 0:
            return False

        for i in range(len(nums)):
            cont_sum += nums[i]

            reminder = cont_sum % k

            if reminder in sum_map and i - sum_map[reminder] >= 2:
                return True
            
            if reminder not in sum_map:
                sum_map[reminder] = i
        
        return False
            

        