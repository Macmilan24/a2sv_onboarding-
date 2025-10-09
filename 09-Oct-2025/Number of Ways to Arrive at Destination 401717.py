# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  
        
        while heap:
            d, node = heapq.heappop(heap)
            
            if d > dist[node]:
                continue
            
            for nei, time in graph[node]:
                new_dist = d + time
                
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_dist, nei))
                
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n - 1] % MOD