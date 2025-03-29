# Problem: Honest Coach - https://codeforces.com/problemset/problem/1360/B

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = list(map(int, input().split()))
    s.sort()
    min_diff = float('inf')
    for i in range(1, n):
        min_diff = min(min_diff, s[i] - s[i - 1])
    print(min_diff)