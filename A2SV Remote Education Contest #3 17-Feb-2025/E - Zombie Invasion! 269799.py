# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    damage = list(map(int, input().split()))
    position = list(map(int, input().split()))

    newDamage = defaultdict(int)
    for i in range(n):
        newDamage[abs(position[i])] += damage[i]

    position = sorted(newDamage.keys())

    prevPosition = 0
    carry = 0

    for i in range(len(position)):
        distance = position[i] - prevPosition
        total = (k * distance) + carry

        if total < newDamage[position[i]]:
            print("NO")
            break 
        
        carry = total - newDamage[position[i]]  
        prevPosition = position[i] 

    else:
        print("YES")
