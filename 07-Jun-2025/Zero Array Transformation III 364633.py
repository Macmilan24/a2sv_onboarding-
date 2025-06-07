# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n + 1:
                diff[r + 1] -= 1
        
        coverage = 0
        for i in range(n):
            coverage += diff[i]
            if coverage < nums[i]:
                return -1

        queries_by_start = [[] for _ in range(n)]
        for l, r in queries:
            queries_by_start[l].append(r)
        
        active_queries_pq = []
        selected_ends_pq = []
        
        num_selected = 0

        for i in range(n):
            for r in queries_by_start[i]:
                heapq.heappush(active_queries_pq, -r)
            
            while selected_ends_pq and selected_ends_pq[0] < i:
                heapq.heappop(selected_ends_pq)
            
            current_coverage = len(selected_ends_pq)
            shortage = nums[i] - current_coverage
            
            if shortage > 0:
                for _ in range(shortage):
                    while active_queries_pq and -active_queries_pq[0] < i:
                        heapq.heappop(active_queries_pq)
                    
                    neg_r = heapq.heappop(active_queries_pq)
                    r = -neg_r
                    
                    num_selected += 1
                    heapq.heappush(selected_ends_pq, r)

        return m - num_selected