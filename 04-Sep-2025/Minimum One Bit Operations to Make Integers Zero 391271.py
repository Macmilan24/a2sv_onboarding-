# Problem: Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        h = n.bit_length() - 1
        return (1 << (h + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << h))