# Problem: A - Stairway to Goodness - https://codeforces.com/gym/608569/problem/A

def max_good_array_length(l, r):
    left, right = 1, 2 * (10**9)
    max_len = 1
    while left <= right:
        mid = (left + right) // 2
        total = (mid - 1) * mid // 2
        if l + total <= r:
            max_len = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_len

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(max_good_array_length(l, r))
