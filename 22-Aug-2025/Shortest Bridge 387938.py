# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direct = [[0,1],[0,-1],[1,0],[-1,0]]

        def inbound(r,c):
            return r < 0 or c < 0 or r == n or c == n

            
        visit = set()
        def dfs(r, c):
            if (inbound(r,c) or not grid[r][c] or (r,c) in visit):
                return
            
            visit.add((r,c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if inbound(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()

                