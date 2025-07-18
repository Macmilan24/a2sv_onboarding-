# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_jump = 0

        for i in range(len(nums)):
            if i > farthest_jump:
                return False
            
            farthest_jump = max(farthest_jump, i + nums[i])
        
        return True