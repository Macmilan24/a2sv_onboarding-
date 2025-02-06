# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        arr = list(s)

        count = arr.count(letter)

        if count == 0:
            return 0
        else:
            return (count * 100) // len(arr)
        