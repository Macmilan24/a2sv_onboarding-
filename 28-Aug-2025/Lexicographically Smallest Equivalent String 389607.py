# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        
        def union(x, y):
            rX, rY = find(x), find(y)
            if rX == rY:
                return 
            
            if rX <= rY:
                parent[rY] = rX 
            else:
                parent[rX] = rY
        
        for char1, char2 in zip(s1, s2):
            union(ord(char1) - ord("a"), ord(char2) - ord("a"))
        
        res = []
        for ch in baseStr:
            root = find(ord(ch) - ord("a"))
            res.append(chr(root + ord("a")))
        
        return "".join(res)
