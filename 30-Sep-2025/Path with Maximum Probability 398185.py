# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        
        heap = [(-1.0, start_node)] 
        
        while heap:
            neg_cur_prob, cur_node = heapq.heappop(heap)
            cur_prob = -neg_cur_prob 

            if cur_node == end_node:
                return cur_prob
            
            if cur_prob < maxProb[cur_node]:
                continue
                
            for neighbor, edge_prob in graph[cur_node]:
                new_prob = cur_prob * edge_prob
             
                if new_prob > maxProb[neighbor]:
                    maxProb[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        
        return 0.0