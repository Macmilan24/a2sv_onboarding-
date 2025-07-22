# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
        
        ancestors = [set() for _ in range(n)]
        
        def bfs(node: int):
            queue = [node]
            visited = {node}
            
            while queue:
                curr = queue.pop(0)
                for parent in graph[curr]:
                    if parent not in visited:
                        ancestors[node].add(parent)
                        queue.append(parent)
                        visited.add(parent)
                        ancestors[node].update(ancestors[parent])
        
        for node in range(n):
            bfs(node)
        
        return [sorted(list(anc)) for anc in ancestors]