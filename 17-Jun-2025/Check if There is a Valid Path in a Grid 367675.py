# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        street = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def inside(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs(x, y):
            if (x, y) == (rows - 1, cols - 1):
                return True

            visited.add((x, y))
            moves = street[grid[x][y]]

            for dx, dy in moves:
                nx = x + dx
                ny = y + dy

                if inside(nx, ny) and (nx, ny) not in visited:
                    back_moves = street[grid[nx][ny]]
                    for bdx, bdy in back_moves:
                        if nx + bdx == x and ny + bdy == y:
                            if dfs(nx, ny):
                                return True
            return False

        return dfs(0, 0)