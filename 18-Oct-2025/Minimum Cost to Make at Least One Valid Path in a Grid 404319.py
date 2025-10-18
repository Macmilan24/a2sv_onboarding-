# Problem: Minimum Cost to Make at Least One Valid Path in a Grid - https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        dq = collections.deque([(0, 0, 0)]) 

        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        while dq:
            cost, r, c = dq.popleft()

            if cost > dist[r][c]:
                continue
            
            if r == m - 1 and c == n - 1:
                return cost

            for sign, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost
                    if sign != grid[r][c]:
                        new_cost += 1
                    
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if sign == grid[r][c]:
                            dq.appendleft((new_cost, nr, nc))
                        else:
                            dq.append((new_cost, nr, nc))
        
        return -1