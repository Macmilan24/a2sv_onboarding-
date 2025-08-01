# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        len_1 = len(word1)
        len_2 = len(word2)
        def dp(i, j):
            if i == len_1:
                return len_2 - j
            if j == len_2:
                return len_1 - i

            
            key = (i, j)

            if key not in memo:
                if word1[i] == word2[j]:
                    memo[key] = dp(i+1, j+1)
                else:
                    insert = 1 + dp(i+1, j)
                    delete = 1 + dp(i, j+1)
                    replace = 1 + dp(i+1, j+ 1)

                    memo[key] = min(insert, delete,replace)
            
            return memo[key]
        
        return  dp(0,0)