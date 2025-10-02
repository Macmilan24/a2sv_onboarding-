# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            it = iter(w)
            waiting[next(it, None)].append(it)

        ans = 0
        for c in s:
            advancing = waiting.pop(c, [])
            for it in advancing:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    ans += 1
        return ans