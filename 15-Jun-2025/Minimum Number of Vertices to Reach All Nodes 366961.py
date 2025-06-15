# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_target = [False] * n 

        for connection in edges:
            start = connection[0]
            end = connection[1]
            is_target[end] = True  

        result = []
        for number in range(n):
            if is_target[number] == False:
                result.append(number) 

        return result