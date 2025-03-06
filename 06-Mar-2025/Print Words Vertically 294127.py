# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len( max(s, key = len))
        res = []

        for i in range(n):
            cur = ""

            for word in s:
                if len(word) > i:
                    cur += word[i]
                else:
                    cur += " "
            
            res.append(cur.rstrip())
        
        return res

        