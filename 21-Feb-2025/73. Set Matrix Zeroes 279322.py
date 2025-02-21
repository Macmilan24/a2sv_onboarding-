# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        zero_row, zero_col = set(), set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_row.add(row)
                    zero_col.add(col)
        
        for row in zero_row:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in zero_col:
            for row in range(rows):
                matrix[row][col] = 0