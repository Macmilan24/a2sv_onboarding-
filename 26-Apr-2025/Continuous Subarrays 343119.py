# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_que = deque()
        max_que = deque()
        res = 0

        for right in range(n):
            while min_que and nums[right] < nums[min_que[-1]]:
                min_que.pop()
            while max_que and nums[right] > nums[max_que[-1]]:
                max_que.pop()
            
            min_que.append(right)
            max_que.append(right)

            while nums[max_que[0]] - nums[min_que[0]] > 2:
                left += 1
                if min_que[0] < left:
                    min_que.popleft()
                if max_que[0] < left:
                    max_que.popleft()
            res += right - left + 1
        return res


            