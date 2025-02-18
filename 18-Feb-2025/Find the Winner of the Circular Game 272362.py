# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = list(range(1, n + 1)) # 1, 2 ,3, 4, 5

        i = 0
        while len(players) > 1:
            i = (i + k - 1) % len(players)
            players.pop(i)
        
        return players[0]



        
