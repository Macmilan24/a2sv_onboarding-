# Problem: B - Wait for Green - https://codeforces.com/gym/623571/problem/B

tests = int(input())
 
for _ in range(tests):
    n, c = input().split()
    s = input()
    n = int(n)
 
    if c == 'g':
        print(0)
        continue
 
    s += s
 
    last = -1
    max_wait = 0
 
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'g':
            last = i
 
        if s[i] == c and last != -1:
            max_wait = max(max_wait, last - i)
 
    print(max_wait)
