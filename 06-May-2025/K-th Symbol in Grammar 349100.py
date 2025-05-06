# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        half = 1 << (n - 2)  
        if k <= half:
            
            return self.kthGrammar(n - 1, k)
        else:
            
            return 1 - self.kthGrammar(n - 1, k - half)