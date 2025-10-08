# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]
            
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for nei, w in graph[node]:
                    new_dist = d + w
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))
            return dist
        
        res_city = -1
        min_count = float('inf')
        
        for i in range(n):
            dist = dijkstra(i)
            reachable = sum(d <= distanceThreshold for d in dist if d != 0)
            if reachable <= min_count:
                min_count = reachable
                res_city = i
        
        return res_city