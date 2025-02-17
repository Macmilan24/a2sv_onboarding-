# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def min_swap(p):
    def binary_helper(left, right):
        if left == right:
            return 0, [p[left]]
        
        mid = (left + right) // 2
        left_count, left_p = binary_helper(left, mid)
        right_count, right_p = binary_helper(mid + 1, right)
        
        if left_count == -1 or right_count == -1:
            return -1, []
        
        if left_p[-1] < right_p[0]:
            return left_count + right_count, left_p + right_p
        elif right_p[-1] < left_p[0]:
            return left_count + right_count + 1, right_p + left_p
        else:
            return -1, []
        
    count, sorted_list = binary_helper(0, len(p) - 1)
    return count

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        results.append(str(min_swap(p)))
    
    print("\n".join(results))

solve()
    