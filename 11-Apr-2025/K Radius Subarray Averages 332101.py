# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        
        if k == 0:
            return nums
        
        window_len = 2 * k + 1
        if window_len > n:
            return avgs
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(k, n - k):
            left = i - k
            right = i + k + 1
            window_sum = prefix[right] - prefix[left]
            avgs[i] = window_sum // window_len
        
        return avgs