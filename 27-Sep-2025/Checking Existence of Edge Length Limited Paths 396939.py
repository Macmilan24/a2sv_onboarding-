# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])

        queries_with_idx = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        queries_with_idx.sort(key=lambda x: x[2]) 

        uf = UnionFind(n)
        res = [False] * len(queries)
        edge_i = 0

        for p, q, limit, qi in queries_with_idx:
            while edge_i < len(edgeList) and edgeList[edge_i][2] < limit:
                u, v, w = edgeList[edge_i]
                uf.union(u, v)
                edge_i += 1
            res[qi] = uf.find(p) == uf.find(q)

        return res