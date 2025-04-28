# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        last_min = nums[0]

        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True

            stack.append([num, last_min])         

            last_min = min(last_min, num)
        
        return False
