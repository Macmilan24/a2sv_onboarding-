# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
    
        def count_overlap(x_shift, y_shift):
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i + x_shift < n and 0 <= j + y_shift < n:
                        if img1[i][j] == 1 and img2[i + x_shift][j + y_shift] == 1:
                            overlap += 1
            return overlap
    
        max_overlap = 0
        for x in range(-n + 1, n):
            for y in range(-n + 1, n):
                current_overlap = count_overlap(x, y)
                max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap