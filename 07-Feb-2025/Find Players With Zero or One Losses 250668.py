# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        zero_lose = []
        one_lose = []

        for match in matches:
            if match[0] not in losses:
                losses[match[0]] = 0
            losses[match[1]] = losses.get(match[1], 0) + 1
        losses = dict(sorted(losses.items()))
        for key, val in losses.items():
            if val == 0:
                zero_lose.append(int(key))
            elif val == 1:
                one_lose.append(int(key))
        
        return [zero_lose, one_lose]

        