# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0

        n = len(firstList)
        m = len(secondList)

        res = []

        while i < n and j < m:
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                res.append([start, end])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
        
        return res

        
        