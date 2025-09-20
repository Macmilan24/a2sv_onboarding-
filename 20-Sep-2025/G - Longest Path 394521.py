# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import deque

def longest_path(N, M, edges):
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for x, y in edges:
        graph[x].append(y)
        indegree[y] += 1

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    dp = [0] * (N+1)
    for u in topo:
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + 1)

    return max(dp)

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
print(longest_path(N, M, edges))