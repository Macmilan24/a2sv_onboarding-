# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        result = 0  
        freq = defaultdict(int)  
        window_base = 0  
        window_start = 0  
        for window_end in range(len(nums)):  
            freq[nums[window_end]] += 1
            while len(freq) > k:
                freq[nums[window_start]] -= 1
                if freq[nums[window_start]] == 0:
                    freq.pop(nums[window_start])
                window_start += 1
                window_base = window_start
            while freq[nums[window_start]] > 1:
                freq[nums[window_start]] -= 1
                window_start += 1
            if len(freq) == k:
                result += (window_start - window_base) + 1

        return result