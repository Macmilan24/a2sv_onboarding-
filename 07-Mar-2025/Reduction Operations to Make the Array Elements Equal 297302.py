# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort()
        num_count = Counter(nums)

        index = 0
        op = 0

        for num, count in num_count.items():
            op += index * count
            index += 1
        
        return op
        