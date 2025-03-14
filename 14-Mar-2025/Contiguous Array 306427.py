# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)/2 == sum(nums):
            return len(nums)
            
        cont_map = {0: -1}

        balance = 0
        max_idx = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1
            
            if balance in cont_map:
                cur_idx = i - cont_map[balance]
                max_idx = max(cur_idx, max_idx)
            else:
                cont_map[balance] = i
        
        return max_idx
        
        print(nums)