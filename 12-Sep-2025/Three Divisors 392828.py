# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        root = int(math.sqrt(n))
        if root * root != n:
            return False
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        
        return is_prime(root)