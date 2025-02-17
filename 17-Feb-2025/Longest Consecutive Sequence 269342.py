# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                current_num = num

                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1
                
                longest = max(longest, count)
        
        return longest
