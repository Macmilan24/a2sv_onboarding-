# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)  

        for eq in equations:
            if eq[1:3] == "==":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                uf.union(a, b)
        
        for eq in equations:
            if eq[1:3] == "!=":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                if uf.find(a) == uf.find(b): 
                    return False
        
        return True