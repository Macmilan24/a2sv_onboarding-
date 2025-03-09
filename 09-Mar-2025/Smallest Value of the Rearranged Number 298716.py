# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        is_negative = num < 0
        num = abs(num)
        
        digits = list(str(num))
        
        if is_negative:
            digits.sort(reverse=True)
        else:
            digits.sort()
            for i in range(len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        
        result = int(''.join(digits))
        
        return -result if is_negative else result