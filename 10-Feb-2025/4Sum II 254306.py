# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        sum_counter = Counter()
        for x in nums1:
            for y in nums2:
                sum_counter[x + y] += 1
        
        total = 0

        for x in nums3:
            for y in nums4:
                total += sum_counter[-(x + y)]
        
        return total