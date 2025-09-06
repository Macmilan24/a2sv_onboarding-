# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()

        for x, y in stones:
            uf.union(x, y + 10001)
        roots = set()
        for x, y in stones:
            roots.add(uf.find(x))
            roots.add(uf.find(y + 10001))

        return len(stones) - len(roots)