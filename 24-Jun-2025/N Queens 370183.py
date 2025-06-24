# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        if n == 2 or n == 3:
            return []

        self.res = []
        board = [['.'] * n for _ in range(n)]
        positions = []

        def dfs(idx, board):
            if idx >= n:
                self.res.append(["".join(row) for row in board])
                return
            
            for i in range(n):
                valid = True
                for q_pos in positions:
                    if q_pos[0] == i or abs(i - q_pos[0]) == abs(idx - q_pos[1]):
                        valid = False
                        break
                
                if not valid:
                    continue
                
                board[i][idx] = 'Q'
                positions.append([i, idx])
                dfs(idx + 1, board )
                positions.pop()
                board[i][idx] = '.'
            
        dfs(0, board)
        return self.res