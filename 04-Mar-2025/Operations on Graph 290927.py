# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)

for _ in range(k):
    operation = list(map(int, input().split()))
    
    if operation[0] == 1:
        u, v = operation[1], operation[2]
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
    
    elif operation[0] == 2: 
        u = operation[1]
        if graph[u]:
            print(" ".join(map(str, graph[u])))
        else:
            print("")
