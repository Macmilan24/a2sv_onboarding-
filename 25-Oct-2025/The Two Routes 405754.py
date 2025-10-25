# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    is_railway = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        is_railway[u][v] = True
        is_railway[v][u] = True
        
    if is_railway[1][n]:
        target_edge_type = False
    else:
        target_edge_type = True
        
    q = deque([(1, 0)])
    visited = {1}
    
    while q:
        curr_node, dist = q.popleft()
        
        if curr_node == n:
            print(dist)
            return
            
        for neighbor in range(1, n + 1):
            if neighbor not in visited:
                if is_railway[curr_node][neighbor] == target_edge_type:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
                    
    print(-1)

solve()