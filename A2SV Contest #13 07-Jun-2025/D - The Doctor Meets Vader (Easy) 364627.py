# Problem: D - The Doctor Meets Vader (Easy) - https://codeforces.com/gym/609279/problem/D

def find_beatable_base(defence_list, attack):
    left = 0
    right = len(defence_list)

    while left < right:
        mid = (left + right) // 2
        if defence_list[mid] <= attack:
            left = mid + 1
        else:
            right = mid
    return left


s, b = map(int, input().split())

ship_attack = list(map(int, input().split()))
base_info = []

for _ in range(b):
    d, g = map(int, input().split())
    base_info.append((d, g))

base_info.sort(key=lambda x: x[0])

sorted_defence = [base[0] for base in base_info]

prefix_gold_sum = [0] * (b + 1)
for i in range(1, b + 1):
    prefix_gold_sum[i] = prefix_gold_sum[i - 1] + base_info[i - 1][1]

res = []

for attack in ship_attack:
    index = find_beatable_base(sorted_defence, attack)
    res.append(prefix_gold_sum[index])

print(*res)
