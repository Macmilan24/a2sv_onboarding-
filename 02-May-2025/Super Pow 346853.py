# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a %= mod

        def mod_pow(base, exp):
            res = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res
        
        res = 1
        for digit in b:
            res = (mod_pow(res, 10) * mod_pow(a, digit)) % mod
        
        return res
        
