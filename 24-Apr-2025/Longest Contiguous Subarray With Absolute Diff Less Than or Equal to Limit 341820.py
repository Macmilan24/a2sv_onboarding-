# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque()
        min_que = deque()

        left = 0
        length = 0

        for right in range(len(nums)):
            while min_que and nums[right] < min_que[-1]:
                min_que.pop()
            while max_que and nums[right] > max_que[-1]:
                max_que.pop()
            
            max_que.append(nums[right])
            min_que.append(nums[right])

            while max_que[0] - min_que[0] > limit:
                if nums[left] == max_que[0]:
                    max_que.popleft()
                if nums[left] == min_que[0]:
                    min_que.popleft()
                left += 1 
            
            length = max(length, right - left + 1)
        
        return length
        