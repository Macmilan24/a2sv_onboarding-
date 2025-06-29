# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        max_score = -1
        result = []
        zeros = 0
        ones = total_ones
        
        for i in range(len(nums) + 1):
            score = zeros + ones
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)
            
            if i < len(nums):
                if nums[i] == 0:
                    zeros += 1
                else:
                    ones -= 1
                    
        return result