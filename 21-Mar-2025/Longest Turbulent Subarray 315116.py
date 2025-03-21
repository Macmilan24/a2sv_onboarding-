# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        max_len = 1
        inc_len = 1
        dec_len = 1

        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                inc_len = dec_len + 1
                dec_len = 1
            elif arr[i - 1] > arr[i]:
                dec_len = inc_len + 1
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1
            
            max_len = max(max_len, dec_len, inc_len)
        
        return max_len