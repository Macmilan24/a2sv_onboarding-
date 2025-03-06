# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        res = []
        intervals.sort()

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]

            res_start, res_end = res[-1]

            if res_end >= cur_start:
                res.pop()
                res.append([res_start, max(res_end, cur_end)])
            else:
                res.append(intervals[i])
        
        return res
        