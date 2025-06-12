# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1:
            return 1
        
        trusts = defaultdict(list)
        trusted = defaultdict(list)

        for a, b in trust:
            trusts[a].append(b)
            trusted[b].append(a)
        
        for person, trust in trusted.items():
            if len(trust) == n - 1 and person not in trusts:
                return person
        
        return -1
