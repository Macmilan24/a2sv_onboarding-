# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        memory = [[-1] * cols for _ in range(rows)]

        def inbound(row, col):
            if 0 <= row < rows and 0 <= col < cols:
                return True
        
        def dfs(row, col):
            if memory[row][col] != -1:
                return memory[row][col]
            
            value = matrix[row][col]
            max_len = 1

            for dx, dy in directions:
                nxt_row = row + dx
                nxt_col = col + dy

                if inbound(nxt_row, nxt_col) and matrix[nxt_row][nxt_col] > value:
                    max_len = max(max_len, 1 + dfs(nxt_row, nxt_col))
            
            memory[row][col] = max_len
            return max_len
        

        longest = 0
        for i in range(rows):
            for j in range(cols):
                longest = max(longest, dfs(i,j))
        
        return longest
        