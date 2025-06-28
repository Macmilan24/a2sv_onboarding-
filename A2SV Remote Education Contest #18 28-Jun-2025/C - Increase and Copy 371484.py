# Problem: C - Increase and Copy - https://codeforces.com/gym/616066/problem/C

import math


def solve():
    n = int(input())
    if n == 1:
        print(0)
        return

    ans = float("inf")

    limit = int(math.sqrt(n)) + 2
    for x in range(1, limit):
        increase_moves = x - 1

        copy_moves = (n + x - 1) // x - 1

        ans = min(ans, increase_moves + copy_moves)

    print(ans)


t = int(input())
for _ in range(t):
    solve()
