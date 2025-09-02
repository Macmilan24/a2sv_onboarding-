# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

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
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        n = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        res = 0
        for indices in groups.values():
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)
            matches = sum((src_count & tgt_count).values())
            res += len(indices) - matches

        return res