# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

import sys

sys.setrecursionlimit(10**6)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * 4 for _ in range(n)]


def solve(d, p):
    if d == n:
        return 0

    if dp[d][p] != -1:
        return dp[d][p]

    res = 0
    for c in range(3):
        if c != p:
            res = max(res, a[d][c] + solve(d + 1, c))

    dp[d][p] = res
    return res


print(solve(0, 3))
