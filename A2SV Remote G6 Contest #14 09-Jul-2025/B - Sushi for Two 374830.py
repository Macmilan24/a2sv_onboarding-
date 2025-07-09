# Problem: B - Sushi for Two - https://codeforces.com/gym/610550/problem/B

n = int(input())
a = list(map(int, input().split()))

blocks = []
count = 1

for i in range(1, n):
    if a[i] == a[i - 1]:
        count += 1
    else:
        blocks.append(count)
        count = 1
blocks.append(count)

res = 0
for i in range(1, len(blocks)):
    res = max(res, 2 * min(blocks[i], blocks[i - 1]))

print(res)
