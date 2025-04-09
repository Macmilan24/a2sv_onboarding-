# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

t = int(input())
for _ in range(t):
    s = input().strip()
    working = set()
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if (j - i) % 2 == 1:
            working.add(s[i])
        i = j
    print("".join(sorted(working)))
