# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        while q:
            next_q = deque()
            for i, j in q:
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if ans[ni][nj] == -1:
                            ans[ni][nj] = ans[i][j] + 1
                            next_q.append((ni, nj))
            q = next_q
        
        return ans