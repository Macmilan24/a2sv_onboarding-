# Problem: C - Clone the Troops - https://codeforces.com/gym/599884/problem/C

t = int(input())
p = 10**9 + 7

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    curr_max = 0
    m = 0
    for x in a:
        curr_max = max(0, curr_max + x)
        m = max(m, curr_max)
    if m > 0:
        t = 1
        for _ in range(k):
            t = (t * 2) % p
        t = (t - 1 + p) % p
        s = (s + t * m) % p
    else:
        s = s % p
    if s < 0:
        s += p
    print(s)
