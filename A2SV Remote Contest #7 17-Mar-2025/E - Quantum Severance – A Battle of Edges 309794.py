# Problem: E - Quantum Severance – A Battle of Edges - https://codeforces.com/gym/596004/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    p_sum = [a[0] if a[0] > 0 else 0]
    n_sum = [abs(a[-1] if a[-1] < 0 else 0)]

    for i in range(1, n):
        p_val = 0
        n_val = 0
        
        if a[i] > 0:
            p_val = a[i]
        
        if a[-(i + 1)] < 0:
            n_val = abs(a[-(i + 1)])
        
        p_sum.append(p_sum[-1] + p_val)
        n_sum.append(n_sum[-1] + n_val)
    
    n_sum.reverse()
    max_val = 0
    for i in range(n):
        cur_max = n_sum[i] + p_sum[i]
        max_val = max(max_val, cur_max)
    
    print(max_val)