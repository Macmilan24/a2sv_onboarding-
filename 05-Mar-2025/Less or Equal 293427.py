# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()



if  k == 0:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
else:
    k_th = nums[k - 1]
    count = sum(1 for num in nums if num <= k_th)
    
    if count == k:
        print(k_th)
    else:
        print(- 1)

    