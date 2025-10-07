# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def buildLPS(pat):
            lps = [0] * len(pat)
            prev = 0
            i = 1
            while i < len(pat):
                if pat[i] == pat[prev]:
                    prev += 1
                    lps[i] = prev
                    i += 1
                else:
                    if prev > 0:
                        prev = lps[prev - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        def kmpSearch(text, pat):
            lps = buildLPS(pat)
            i = j = 0
            while i < len(text):
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == len(pat):
                        return True
                else:
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False
        
        repeated = a
        count = 1
        while len(repeated) < len(b):
            repeated += a
            count += 1
        
        if kmpSearch(repeated, b):
            return count
        
        if kmpSearch(repeated + a, b):
            return count + 1
        
        return -1