# Problem: D - Split the Difference! - https://codeforces.com/gym/622136/problem/D

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k > n:
        print(0)
        return

    total_cost = a[n - 1] - a[0]

    diffs = []

    for i in range(n - 1):
        diffs.append(a[i + 1] - a[i])

    diffs.sort(reverse=True)
    for i in range(k - 1):
        total_cost -= diffs[i]

    print(total_cost)


solve()
