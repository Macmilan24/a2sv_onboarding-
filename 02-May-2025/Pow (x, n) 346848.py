# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        
        res = 1.0
        cur_pro = x

        while n > 0:
            if n % 2 == 1:
                res *= cur_pro
            cur_pro *= cur_pro
            n //= 2
        
        return res
