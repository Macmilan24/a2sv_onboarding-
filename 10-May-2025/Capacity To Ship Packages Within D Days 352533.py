# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            d = 1
            current = 0

            for weight in weights:
                if current + weight > mid:
                    d += 1  
                    current = 0
                current += weight

            if d > days:
                left = mid + 1
            else:
                right = mid

        return left