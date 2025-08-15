# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())
    h = list(map(int, sys.stdin.readline().split()))

    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                cost = dp[i - j] + abs(h[i] - h[i - j])
                dp[i] = min(dp[i], cost)

    print(dp[n - 1])


solve()
