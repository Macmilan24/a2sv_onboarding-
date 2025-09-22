# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        a.sort()
        ok = True
        for i in range(1, n):
            if a[i] - a[i - 1] > 1:
                ok = False
                break
        print("YES" if ok else "NO")


solve()
