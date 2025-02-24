# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

def draw_snake(n, m):
    grid = [['.' for _ in range(m)] for _ in range(n)]
    for c in range(m):
        grid[0][c] = '#'
    for r in range(1, n):
        if r % 2 == 0:
            for c in range(m):
                grid[r][c] = '#'
        else:
            if (r // 2) % 2 == 0:
                grid[r][m-1] = '#'
            else:
                grid[r][0] = '#'
    for row in grid:
        print(''.join(row))

n, m = map(int, input().split())
draw_snake(n, m)