# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total_hours = sum(math.ceil(pile / mid) for pile in piles)


            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left