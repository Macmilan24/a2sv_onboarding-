# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = Counter(nums)

        target = 0
        for color in range(3):
            count = color_count[color]
            for _ in range(count):
                nums[target] = color
                target += 1
