# Problem: A - Twice - https://codeforces.com/gym/619446/problem/A

from collections import Counter

def solve():

    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)

    score = 0

    for count in counts.values():
        score += count // 2

    print(score)


t = int(input())

for _ in range(t):
    solve()
