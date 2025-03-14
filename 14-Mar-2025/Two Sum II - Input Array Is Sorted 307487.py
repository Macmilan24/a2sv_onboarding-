# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur = numbers[left] + numbers[right]

            if cur < target:
                left += 1
            elif cur > target:
                right -= 1
            else:
                return [left + 1, right + 1]