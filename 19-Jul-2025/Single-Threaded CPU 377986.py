# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_heap = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        
        heapq.heapify(task_heap)
        
        available_tasks = []
        current_time = 0
        result_order = []
        while task_heap or available_tasks:
            while task_heap and task_heap[0][0] <= current_time:

                enqueue, process, index = heapq.heappop(task_heap)
                heapq.heappush(available_tasks, (process, index, enqueue))

            if available_tasks:

                process, index, enqueue = heapq.heappop(available_tasks)
                result_order.append(index)
                current_time += process
                
            elif task_heap:
                current_time = task_heap[0][0]
        return result_order