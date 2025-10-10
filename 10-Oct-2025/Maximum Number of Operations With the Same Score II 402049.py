# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 2:
            return 0

        memo = {}

        def dfs(i, j, target):
            if i >= j:
                return 0
            key = (i, j, target)
            if key in memo:
                return memo[key]

            res = 0
            if i + 1 <= j and nums[i] + nums[i + 1] == target:
                res = max(res, 1 + dfs(i + 2, j, target))

            if j - 1 >= i and nums[j - 1] + nums[j] == target:
                res = max(res, 1 + dfs(i, j - 2, target))

            if nums[i] + nums[j] == target:
                res = max(res, 1 + dfs(i + 1, j - 1, target))

            memo[key] = res
            return res

        return max(
            dfs(0, n - 1, nums[0] + nums[1]),
            dfs(0, n - 1, nums[-2] + nums[-1]),
            dfs(0, n - 1, nums[0] + nums[-1])
        )
