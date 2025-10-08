# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def buildLPS(pattern):
            lps = [0] * len(pattern)
            prev = 0 
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[prev]:
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

        if not needle:
            return 0

        lps = buildLPS(needle)

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1