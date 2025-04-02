# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        total_pairs = 0
        result = 0

        for right in range(len(nums)):
            total_pairs += count[nums[right]]
            count[nums[right]] += 1

            while total_pairs >= k:
                result += len(nums) - right
                total_pairs -= count[nums[left]] - 1
                count[nums[left]] -= 1
                left += 1

        return result