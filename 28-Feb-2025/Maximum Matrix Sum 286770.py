# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_neg = float("inf")
        neg_count = 0

        for row in matrix:
            for num in row:
                total += abs(num)
                min_neg = min(min_neg, abs(num))
                if num < 0:
                    neg_count += 1
                
        
        if neg_count & 1:
            total -= 2 * min_neg
        
        return total