# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.range = [0] * (n + 1)

        for i in range(1, n + 1):
            self.range[i] = self.range[i - 1] + nums[i - 1]

        

    def sumRange(self, left: int, right: int) -> int:
        return self.range[right + 1] - self.range[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)