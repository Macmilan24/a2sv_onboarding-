# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)

        coins = 0

        for i in range(1, (len(piles) - len(piles) // 3), 2):
            coins += piles[i]
        
        return coins