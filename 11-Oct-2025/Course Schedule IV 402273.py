# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        preReqs = [set() for _ in range(numCourses)]
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while q:
            course = q.popleft()
            
            for nxt in graph[course]:
                preReqs[nxt].add(course)
                preReqs[nxt].update(preReqs[course])  
                
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        res = []
        for u, v in queries:
            res.append(u in preReqs[v])
        return res