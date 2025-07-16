# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        points.sort() 

        arrow_count = 0
        current_end = points[0][1]
        for i in range(1, len(points)):
            start_point = points[i][0]
            end_point = points[i][1]
            if start_point <= current_end:
                current_end = min(current_end, end_point)
            else:
                arrow_count += 1
                current_end = end_point
        arrow_count += 1
        return arrow_count