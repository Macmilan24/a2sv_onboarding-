# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])

        trans_matrix = [[0] * m for _ in range(n)]

        
        for i, nums in enumerate(matrix):
            for j in range(len(nums)):
               trans_matrix[j][i] = nums[j]

        return trans_matrix

        