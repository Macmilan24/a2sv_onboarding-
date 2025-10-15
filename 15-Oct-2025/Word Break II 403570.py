# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)  
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]  
            
            if start in memo:
                return memo[start]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for rest in dfs(end):
                        if rest:
                            res.append(word + " " + rest)
                        else:
                            res.append(word)
            
            memo[start] = res
            return res
        
        return dfs(0)