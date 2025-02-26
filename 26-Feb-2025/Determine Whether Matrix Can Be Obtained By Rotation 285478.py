# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
    
        def rotate():
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for i in range(n):
                mat[i].reverse()
        
        def check():
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            return True
        
        for _ in range(4):
            if check():
                return True
            rotate()
        
        return False