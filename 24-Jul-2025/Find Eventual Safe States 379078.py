# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = defaultdict(list)
        in_degree = [0] * n

        for src in range(n):
            for dest in graph[src]:
                reversed_graph[dest].append(src)
                in_degree[src] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in reversed_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(i for i in range(n) if safe[i])