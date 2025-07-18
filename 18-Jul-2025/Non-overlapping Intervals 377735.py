# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_remove = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]

            if cur_start >= prev_end:
                prev_end = cur_end
            else:
                min_remove += 1
                prev_end = min(prev_end, cur_end)
        
        return min_remove

            