# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def dfs(city):
            seen.add(city)
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in seen:
                    dfs(nei)

        count = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1

        return count