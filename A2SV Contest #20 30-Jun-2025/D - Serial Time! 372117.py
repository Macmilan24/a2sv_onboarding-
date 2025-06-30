# Problem: D - Serial Time! - https://codeforces.com/gym/618729/problem/D

def dfs(height, row, col):
    if not (0 <= height < k and 0 <= row < n and 0 <= col < m):
        return 0

    if plate[height][row][col] == "#":
        return 0

    plate[height][row][col] = "#"

    volume = 1

    volume += dfs(height + 1, row, col)
    volume += dfs(height - 1, row, col)
    volume += dfs(height, row + 1, col)
    volume += dfs(height, row - 1, col)
    volume += dfs(height, row, col + 1)
    volume += dfs(height, row, col - 1)

    return volume


k, n, m = map(int, input().split())

input()

plate = []

for _ in range(k):
    layer = [list(input()) for _ in range(n)]
    plate.append(layer)

    input()



x, y = map(int, input().split())

start_row = x - 1
start_col = y - 1
start_height = 0

total_min = dfs(start_height, start_row, start_col)
print(total_min)
