# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_map = {}
        res = []

        for num in reversed(nums2):
            while stack:
                if stack[-1] > num:
                    num_map[num] = stack[-1]
                    stack.append(num)
                    break
                else:
                    stack.pop()
            
            if len(stack) == 0:
                num_map[num] = -1
                stack.append(num)
        
        for num in nums1:
            res.append(num_map[num])
        return res