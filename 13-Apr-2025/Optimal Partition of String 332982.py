# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        count = 0

        for ch in s:
            if ch in visited:
                count += 1
                visited.clear()
            visited.add(ch)
        
        return count + 1