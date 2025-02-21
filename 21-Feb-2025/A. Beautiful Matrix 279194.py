# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A


for i in range(5):
    row = input().split()
    if '1' in row:
        print(abs(2 - row.index('1')) + abs(2 - i))
        break