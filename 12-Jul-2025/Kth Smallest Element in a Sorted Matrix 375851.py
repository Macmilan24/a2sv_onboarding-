# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 0:
            return None

        min_heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)} 
        for i in range(k):
            value, row, col = heappop(min_heap)
            if i == k - 1:
                return value

            if col + 1 < n and (row, col + 1) not in visited:
                heappush(min_heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))

            if col == 0 and row + 1 < n and (row + 1, 0) not in visited:
                heappush(min_heap, (matrix[row + 1][0], row + 1, 0))
                visited.add((row + 1, 0))
        
        return None