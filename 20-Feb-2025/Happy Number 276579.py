# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:

            if n in seen:
                return False
            
            seen.add(n)

            sum_squr = 0

            while n > 0:
                digit = n % 10
                sum_squr += digit * digit
                n = n // 10
            
            n = sum_squr
        
        return True