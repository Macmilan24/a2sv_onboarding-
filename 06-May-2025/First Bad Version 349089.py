# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        first_bad = n

        while left <= right:
            mid = (left + right) // 2
            response = isBadVersion(mid)

            if response:
                right = mid - 1
                first_bad = min(first_bad, mid)
            else:
                left = mid + 1
        
        return first_bad

        