# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
p = list(map(float, input().split()))

dp = [0.0] * (N + 1)
dp[0] = 1.0  

for i in range(N):
    next_dp = [0.0] * (N + 1)
    for k in range(i + 1):
        next_dp[k] += dp[k] * (1 - p[i])
        
        next_dp[k + 1] += dp[k] * p[i]
    dp = next_dp

ans = sum(dp[N // 2 + 1 :])
print(ans)
