# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degree = [0] * (n + 1) 

for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1

count = degree[1:]

if all(d == count[0] for d in count):
    print("YES")
else:
    print("NO")
