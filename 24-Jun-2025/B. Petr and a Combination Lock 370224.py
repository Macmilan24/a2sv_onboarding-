# Problem: B. Petr and a Combination Lock - https://codeforces.com/contest/1097/problem/B

solved = False


def dfs(n, curr, combination):
    global solved
    if n == 0:
        if curr % 360 == 0:
            solved = True
        return

    dfs(n - 1, curr + combination[n - 1], combination)
    dfs(n - 1, curr - combination[n - 1], combination)


n = int(input())
combination = [int(input()) for _ in range(n)]

dfs(n, 0, combination)

if solved:
    print("YES")
else:
    print("NO")
