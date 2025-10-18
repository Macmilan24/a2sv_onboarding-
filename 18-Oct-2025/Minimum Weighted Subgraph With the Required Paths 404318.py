# Problem: Minimum Weighted Subgraph With the Required Paths - https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj = collections.defaultdict(list)
        rev_adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))

        def dijkstra(start_node, graph_adj):
            dist = [float('inf')] * n
            dist[start_node] = 0
            pq = [(0, start_node)]

            while pq:
                d, u = heapq.heappop(pq)

                if d > dist[u]:
                    continue

                for v, w in graph_adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist

        dist1 = dijkstra(src1, adj)
        dist2 = dijkstra(src2, adj)
        dist_dest = dijkstra(dest, rev_adj)

        min_weight = float('inf')
        for i in range(n):
            if dist1[i] != float('inf') and dist2[i] != float('inf') and dist_dest[i] != float('inf'):
                min_weight = min(min_weight, dist1[i] + dist2[i] + dist_dest[i])

        return min_weight if min_weight != float('inf') else -1