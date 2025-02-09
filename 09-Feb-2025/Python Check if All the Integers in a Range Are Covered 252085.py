# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for i in range(left, right + 1):
            if not any(l <= i <= r for l, r in ranges):
                return False
        
        return True
                    

        