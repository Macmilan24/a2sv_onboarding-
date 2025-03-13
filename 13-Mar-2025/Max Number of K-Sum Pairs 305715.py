# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        freq = Counter(nums)
        count = 0

        for num in freq.keys():
            if num * 2 == k:
                count += freq[num] // 2
            elif k - num in freq and num > k - num:
                count += min(freq[k - num], freq[num])
        
        return count


