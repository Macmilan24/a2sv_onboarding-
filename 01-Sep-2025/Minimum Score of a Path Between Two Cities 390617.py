# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i 
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v, dist in roads:
            uf.union(u - 1, v - 1)
        
        min_score = float('inf')

        root_of_1 = uf.find(0)

        for u, v, dist in roads:
            if uf.find(u - 1) == root_of_1:
                min_score = min(min_score, dist)
        
        return min_score