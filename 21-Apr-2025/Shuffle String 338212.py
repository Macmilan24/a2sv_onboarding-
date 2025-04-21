# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_str = [""]*len(indices)
        for char, i in zip(s,indices):
            shuffled_str[i] = char
        return "".join(shuffled_str)

        