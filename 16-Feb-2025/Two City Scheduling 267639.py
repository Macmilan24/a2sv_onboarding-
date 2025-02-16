# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key = lambda x:x[0] - x[1])
        
        min_cost = 0

        print(costs)

        n = len(costs) // 2 
        for i in range(2 * n):
            if i < n:
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]
        
        return min_cost

        
        