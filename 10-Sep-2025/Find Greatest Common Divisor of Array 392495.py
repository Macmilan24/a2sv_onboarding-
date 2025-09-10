# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        smallest = min(nums)
        largest = max(nums)
        return gcd(smallest, largest)