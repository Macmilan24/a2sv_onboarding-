# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

n = int(input())
heights = list(map(int, input().split()))

max_left = [0] * n
min_right = [0] * n

max_left[0] = heights[0]
for i in range(1, n):
    max_left[i] = max(max_left[i - 1], heights[i])

min_right[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    min_right[i] = min(min_right[i + 1], heights[i])

count = 0
for i in range(n - 1):
    if max_left[i] <= min_right[i + 1]:
        count += 1

print(count + 1)
