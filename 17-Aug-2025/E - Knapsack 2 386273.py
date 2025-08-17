# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

n, W = map(int, input().split())
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
max_value = 0
for w, v in items:
    max_value += v
N = n + 1
V = max_value + 1
dp = []
for i in range(N):
    row = []
    for j in range(V):
        row.append(float("inf"))
    dp.append(row)
dp[0][0] = 0
i = 1
while i < N:
    w, v = items[i - 1]
    j = 0
    while j < V:
        if dp[i - 1][j] < dp[i][j]:
            dp[i][j] = dp[i - 1][j]
        if j >= v:
            if dp[i - 1][j - v] + w < dp[i][j]:
                dp[i][j] = dp[i - 1][j - v] + w
        j += 1
    i += 1
ans = 0
k = V - 1
while k >= 0:
    if dp[N - 1][k] <= W:
        ans = k
        break
    k -= 1
print(ans)
