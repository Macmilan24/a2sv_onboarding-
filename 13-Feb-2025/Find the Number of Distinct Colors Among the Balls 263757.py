# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        frequency = Counter()

        colors = {}

        ans = []

        for x, y in queries:
            if x in colors:
                frequency[colors[x]] -= 1

                if frequency[colors[x]] == 0:
                    del frequency[colors[x]]
            
            frequency[y] += 1
            colors[x] = y
            ans.append(len(frequency))
        
        return ans