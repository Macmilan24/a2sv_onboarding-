# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        possible = {0} 
        for stone in stones:
            new_sums = set()
            for s in possible:
                new_sums.add(s + stone)
                new_sums.add(s)
            possible = new_sums
        
        best = 0
        for s in possible:
            if s <= target:
                best = max(best, s)
        
        return total_sum - 2 * best