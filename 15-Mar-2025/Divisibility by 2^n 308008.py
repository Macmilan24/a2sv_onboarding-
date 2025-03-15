# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def count_twos(x):
    twos = 0
    while x % 2 == 0:
        twos += 1
        x //= 2
    return twos

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    

    current_twos = sum(count_twos(x) for x in a)
    
    extra = [count_twos(i + 1) for i in range(n)]  
    extra.sort(reverse=True)  

    if current_twos >= n:
        print(0)
    elif current_twos + sum(extra) < n:
        print(-1)
    else:
        need = n - current_twos
        ops = 0
        total_extra = 0
        for e in extra:
            total_extra += e
            ops += 1
            if total_extra >= need:
                print(ops)
                break