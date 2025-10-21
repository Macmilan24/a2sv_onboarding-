# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = reduce(gcd, nums)
        # If gcd == 1, we can form 1 as a linear combination
        return g == 1