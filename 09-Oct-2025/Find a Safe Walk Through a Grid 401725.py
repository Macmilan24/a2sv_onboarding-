# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        startHealth = health - grid[0][0]
        if startHealth < 1:
            return False
        
        bestHealth = [[-1] * n for _ in range(m)]
        bestHealth[0][0] = startHealth
        
        pq = [(-startHealth, 0, 0)]  
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while pq:
            negH, x, y = heapq.heappop(pq)
            h = -negH
            
            if x == m-1 and y == n-1 and h >= 1:
                return True
            
            if h < bestHealth[x][y]:
                continue
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh < 1:
                        continue
                    if nh > bestHealth[nx][ny]:
                        bestHealth[nx][ny] = nh
                        heapq.heappush(pq, (-nh, nx, ny))
        
        return False