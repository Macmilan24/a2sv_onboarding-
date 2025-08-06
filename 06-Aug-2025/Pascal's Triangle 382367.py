# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        for row in range(numRows):
            cur_row = [1] * (row + 1)
            for j in range(1, row):
                cur_row[j] = triangle[row-1][j-1] + triangle[row-1][j]
            triangle.append(cur_row)
        return triangle