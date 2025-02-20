# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def not_similar(str1, str2):
            for s in str1:
                if s in str2:
                    return False
            return True

        max_len = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not_similar(words[i], words[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        
        return max_len
        