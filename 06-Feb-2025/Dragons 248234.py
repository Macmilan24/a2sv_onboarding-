# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

strength, t = map(int, input().split())
dragons = []

for _ in range(t):
    dragon_strength, bonus = map(int, input().split())
    dragons.append((dragon_strength, bonus))

dragons.sort()

for dragon_strength, bonus in dragons:
    if strength > dragon_strength:
        strength += bonus 
    else:
        print("NO")
        exit() 

print("YES")
