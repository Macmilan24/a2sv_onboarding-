# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = emp

        def dfs(eid):
            e = emp_map[eid]
            total = e.importance
            for sub in e.subordinates:
                total += dfs(sub)
            return total

        return dfs(id)