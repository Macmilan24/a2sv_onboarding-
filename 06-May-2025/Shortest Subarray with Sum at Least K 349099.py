# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        queue = deque()
        min_len = n + 1
        
        for i in range(len(prefix_sum)):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_len = min(min_len, i - queue.popleft())
            
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()
            
            queue.append(i)
        
        return min_len if min_len <= n else -1
