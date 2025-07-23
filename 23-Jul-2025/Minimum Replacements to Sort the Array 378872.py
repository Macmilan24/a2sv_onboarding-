# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        total_op = 0
        right_limit = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            current = nums[i]

            if current <= right_limit:
                right_limit = current
            else:
                parts = (current + right_limit - 1) // right_limit
                total_op += parts - 1
                right_limit = current // parts

        return total_op