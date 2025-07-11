# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for _ in range(k):
            cur = -heapq.heappop(heap)
            cur -= cur // 2

            heapq.heappush(heap, -cur)
        
        return -sum(heap)