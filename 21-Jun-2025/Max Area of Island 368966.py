# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0 or (x, y) in seen:
                return 0
            seen.add((x, y))
            size = 1
            size += dfs(x + 1, y)
            size += dfs(x - 1, y)
            size += dfs(x, y + 1)
            size += dfs(x, y - 1)
            return size

        biggest = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in seen:
                    area = dfs(i, j)
                    if area > biggest:
                        biggest = area

        return biggest