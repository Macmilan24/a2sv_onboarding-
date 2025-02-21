# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):

                hourglass = (
                    grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] +
                    grid[row][col] +
                    grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]
                )

                max_sum = max(max_sum, hourglass)
        
        return max_sum