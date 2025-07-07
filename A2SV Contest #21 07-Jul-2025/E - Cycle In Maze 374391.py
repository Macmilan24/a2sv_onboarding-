# Problem: E - Cycle In Maze - https://codeforces.com/gym/619446/problem/E

from collections import deque


def solve():
    n, m, k = map(int, input().split())
    grid = []
    start = None
    for i in range(n):
        row = list(input().rstrip())
        for j, c in enumerate(row):
            if c == "X":
                start = (i, j)
                row[j] = "."
        grid.append(row)

    dist = [[-1] * m for _ in range(n)]
    dq = deque([start])
    dist[start[0]][start[1]] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "." and dist[nx][ny] < 0:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))

    if k % 2 != 0:
        print("IMPOSSIBLE")
        return

    x, y = start
    res = []
    moves = [("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0)]
    for step in range(k):
        found = False
        for ch, dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == ".":

                rem = k - step - 1
                if dist[nx][ny] >= 0 and dist[nx][ny] <= rem:
                    res.append(ch)
                    x, y = nx, ny
                    found = True
                    break
        if not found:
            print("IMPOSSIBLE")
            return
    print("".join(res))


solve()
