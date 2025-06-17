# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        seen = set()

        def dfs(x, y):
            if x < 0 or x >= h or y < 0 or y >= w or grid[x][y] == 0:
                return 1
            if (x, y) in seen:
                return 0

            seen.add((x, y))
            ans = 0
            ans += dfs(x+1, y)
            ans += dfs(x-1, y)
            ans += dfs(x, y+1)
            ans += dfs(x, y-1)
            return ans

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0