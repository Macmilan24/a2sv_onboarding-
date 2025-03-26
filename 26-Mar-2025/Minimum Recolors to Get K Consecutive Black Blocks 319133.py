# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')

        current_white = blocks[:k].count('W')
        min_operations = current_white

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_white -= 1
            if blocks[i] == 'W':
                current_white += 1
            min_operations = min(min_operations, current_white)
        
        return min_operations