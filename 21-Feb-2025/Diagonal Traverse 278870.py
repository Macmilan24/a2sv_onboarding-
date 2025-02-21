# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        row = len(mat)
        col = len(mat[0])

        diagonal_list = []

        cur_row = cur_col = 0
        up_dir = True

        while len(diagonal_list) != row * col:
            if up_dir:
                while cur_row >= 0 and cur_col < col:
                    diagonal_list.append(mat[cur_row][cur_col])

                    cur_row -= 1
                    cur_col += 1

                if cur_col == col:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                up_dir = False    
            else:
                while cur_col >= 0 and cur_row < row:
                    diagonal_list.append(mat[cur_row][cur_col])

                    cur_col -= 1
                    cur_row += 1
                
                if cur_row == row:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                up_dir = True
        
        return diagonal_list

