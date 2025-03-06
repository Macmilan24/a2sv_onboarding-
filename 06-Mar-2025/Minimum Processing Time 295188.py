# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)

        min_PT = 0

        for i in range(len(processorTime)):

            task_group = tasks[i*4 : i*4 + 4]

            finished = processorTime[i] + max(task_group)

            min_PT = max(min_PT, finished)
        
        return min_PT