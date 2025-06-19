# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, col):
            color[node] = col
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - col):
                        return False
                elif color[nei] == col:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True