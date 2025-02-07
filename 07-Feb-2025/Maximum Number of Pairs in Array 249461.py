# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        hashmap = {}
        pair = 0
        leftover = 0

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for count in hashmap.values():
            pair += count // 2
            leftover += count % 2
        
        return [pair, leftover]
        