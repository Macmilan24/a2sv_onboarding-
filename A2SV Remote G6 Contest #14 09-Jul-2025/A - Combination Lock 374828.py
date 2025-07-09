# Problem: A - Combination Lock - https://codeforces.com/gym/610550/problem/A

n = int(input())
original = input()
target = input()

moves = 0

for i in range(n):
    o = int(original[i])
    t = int(target[i])
    diff = abs(o - t)
    moves += min(diff, 10 - diff)
print(moves)