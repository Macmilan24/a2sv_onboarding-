# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def even_odd():
            left = 0 
            max_len = 1

            for right in range(1, len(arr)):
                if (right % 2 == 0 and arr[right - 1] <= arr[right]) or (right % 2 == 1 and arr[right - 1] >= arr[right]):
                    left = right
                
                max_len = max(max_len, right - left + 1)
            
            return max_len
        
        def odd_even():
            left = 0 
            max_len = 1

            for right in range(1, len(arr)):
                if (right % 2 == 1 and arr[right - 1] <= arr[right]) or (right % 2 == 0 and arr[right - 1] >= arr[right]):
                    left = right
                
                max_len = max(max_len, right - left + 1)
            
            return max_len

        return max(odd_even(), even_odd())
            
        