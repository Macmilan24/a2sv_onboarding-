# Problem: F - Luffy’s Lineup Challenge - https://codeforces.com/gym/594356/problem/F

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    swaps = []

    for i in range(n):
        if b[i] != a[i]:
            j = i + 1
            while j < n and b[j] != a[i]:
                j += 1
            
            
            while j > i:
                b[j], b[j - 1] = b[j - 1], b[j]
                swaps.append((j, j + 1))
                j -= 1

    print(len(swaps))
    for p1, p2 in swaps:
        print(p1, p2)

solve()