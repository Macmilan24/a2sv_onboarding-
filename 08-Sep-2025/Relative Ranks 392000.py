# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [""] * n

        indexed = [(s, i) for i, s in enumerate(score)]
        indexed.sort(reverse=True, key=lambda x: x[0])

        for rank, (_, i) in enumerate(indexed, start=1):
            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)

        return res