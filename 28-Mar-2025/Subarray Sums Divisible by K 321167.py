# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        subarray_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            reminder = ((prefix_sum % k) + k)% k

            count += subarray_count.get(reminder, 0)
            subarray_count[reminder] = subarray_count.get(reminder, 0) + 1
        
        return count

        