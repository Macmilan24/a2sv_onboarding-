# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.p = [0] * (n + 1)

        for i in range(1, n + 1):
            self.p[i] = self.p[i - 1] + nums[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right + 1] - self.p[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)