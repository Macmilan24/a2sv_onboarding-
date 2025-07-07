# Problem: B - AB Flipping - https://codeforces.com/gym/619446/problem/B


def solve():
    n = int(input())
    s = input()

    first_a = -1
    for i in range(n):
        if s[i] == "A":
            first_a = i
            break

    last_b = -1

    for i in range(n - 1, -1, -1):
        if s[i] == "B":
            last_b = i
            break

    if first_a == -1 or last_b == -1 or first_a > last_b:
        print(0)

    else:
        print(last_b - first_a)


t = int(input())
for _ in range(t):
    solve()
