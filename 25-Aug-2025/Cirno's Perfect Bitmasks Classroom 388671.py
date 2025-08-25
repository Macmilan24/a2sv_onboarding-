# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def lowest_bit(x):
    return x & -x

t = int(input())
for _ in range(t):
    x = int(input())
    if x == 1:
        print(3)
        continue
    lb = lowest_bit(x)
    if x == lb:
        print(x + 1)
    else:
        print(lb)
