# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        my_coin = 0
        
        for i in range(len(piles) // 3, len(piles), 2):
            my_coin += piles[i]
        
        return my_coin

        