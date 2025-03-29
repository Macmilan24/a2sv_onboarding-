# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
max_temp = 200001
events = [0] * max_temp

for _ in range(n):
    l, r = map(int, input().split())
    events[l] += 1
    if r + 1 < max_temp:
        events[r + 1] -= 1


votes = [0] * max_temp
votes[0] = events[0]
for i in range(1, max_temp):
    votes[i] = votes[i-1] + events[i]

admissible = [0] * max_temp
for i in range(1, max_temp):
    admissible[i] = 1 if votes[i] >= k else 0


prefix = [0] * max_temp
for i in range(1, max_temp):
    prefix[i] = prefix[i-1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])