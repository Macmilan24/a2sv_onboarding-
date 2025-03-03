# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
res = []

while i < n or j < m:
    if j == m or (i < n and a[i] < b[j]):
        i += 1
    else:
        res.append(i)
        j += 1

print(*res)