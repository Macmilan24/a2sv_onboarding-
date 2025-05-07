# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            total = sum(math.ceil(num / mid) for num in nums)

            if total <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left