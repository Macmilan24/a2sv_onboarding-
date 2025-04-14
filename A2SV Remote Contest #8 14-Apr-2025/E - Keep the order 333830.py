# Problem: E - Keep the order - https://codeforces.com/gym/599884/problem/E

n = int(input())
enter = list(map(int, input().split()))
exit = list(map(int, input().split()))

exit_pos = {troop: i for i, troop in enumerate(exit)}

fired = 0
max_exit = -1

for troop in enter:
    if exit_pos[troop] > max_exit:
        max_exit = exit_pos[troop]
    else:
        fired += 1

print(fired)