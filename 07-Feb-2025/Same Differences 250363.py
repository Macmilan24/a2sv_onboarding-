# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t = int(input())

for _ in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
        
    hashmap = {}
    count = 0
        
    for i in range(length):
        val = nums[i] - i
        if val in hashmap:
            count += hashmap[val]
            hashmap[val] += 1
        else:
            hashmap[val] = 1
    print(count)