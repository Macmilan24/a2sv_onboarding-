# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0 

        for start in nums:
            length = 1       
            current = start  

            while current * current <= 100000:  
                next_num = current * current    
                if next_num in num_set:         
                    length += 1                 
                    current = next_num          
                else:
                    break              

            longest = max(longest, length)

        return longest if longest >= 2 else -1