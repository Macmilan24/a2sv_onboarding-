# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            grid = [[0]*col for _ in range(row)]
            
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1 
            
            q = deque()
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = -1  
            
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                r, c = q.popleft()
                if r == row-1: 
                    return True
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        q.append((nr,nc))
            return False

        lo, hi = 1, row*col
        ans = 0
        while lo <= hi:
            mid = (lo+hi)//2
            if can_cross(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans