# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        def binary_search(starts, end):
            left = 0
            right = len(starts) - 1
            start_j = -1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    start_j = starts[mid][1]
                    right = mid - 1

                else:
                    left = mid + 1
            
            return start_j

        starts = []
        res = []

        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))
        
        starts.sort()

        for start_j, end_j in intervals:
            index = binary_search(starts, end_j)
            res.append(index)
        
        return res

