# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))

odd = False
even = False

for i in range(len(a)):
    if a[i] % 2 == 0:
        even = True
    else:
        odd = True

if odd and even:
    a.sort()

print(*a)
