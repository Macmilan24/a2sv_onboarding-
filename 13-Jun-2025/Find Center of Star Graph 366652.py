# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = {}

        for edge in edges:
            a, b = edge[0], edge[1]

            if a in count:
                count[a] += 1
            else:
                count[a] = 1

            if b in count:
                count[b] += 1
            else:
                count[b] = 1

        for key in count:
            if count[key] == len(edges):
                return key