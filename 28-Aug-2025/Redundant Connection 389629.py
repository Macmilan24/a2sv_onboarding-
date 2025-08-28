# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rX, rY = find(x), find(y)
            if rX == rY:
                return False
            
            if rank[rX] < rank[rY]:
                parent[rX] = rY
                rank[rY] += rank[rX]
            else:
                parent[rY] = rX
                rank[rX] += rank[rY]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        