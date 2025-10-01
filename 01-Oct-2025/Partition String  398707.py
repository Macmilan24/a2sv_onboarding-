# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        cur = ""

        for c in s:
            cur += c
            if cur not in seen:
                seen.add(cur)
                res.append(cur)
                cur = ""

        return res