# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c, minute = queue.popleft()
            time = max(time, minute)
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minute + 1))

        return time if fresh == 0 else -1