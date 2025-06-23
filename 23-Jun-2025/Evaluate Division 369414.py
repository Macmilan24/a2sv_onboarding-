# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def dfs(curr, target, visited):
            if curr not in adj or target not in adj:
                return -1.0
            if curr == target:
                return 1.0
            visited.add(curr)

            for neighbor, weight in adj[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0

        results = []
        for x, y in queries:
            results.append(dfs(x, y, set()))

        return results