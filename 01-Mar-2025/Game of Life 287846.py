# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def countNeighbors(r, c):
            neighbour  = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols  ):
                        continue 
                    if board[i][j] in [1, 3]:
                        neighbour += 1
            
            return neighbour 
        
        for row in range(rows):
            for col in range(cols):
                neighbour  = countNeighbors(row, col)
                if board[row][col]:
                    if neighbour in [2, 3]:
                        board[row][col] = 3
                elif neighbour == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1