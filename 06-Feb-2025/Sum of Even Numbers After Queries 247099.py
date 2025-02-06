# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = sum(num for num in nums if num % 2 == 0)

        for val, index in queries:
            old_val = nums[index]

            if old_val % 2 == 0:
                even_sum -= old_val
            
            nums[index] += val

            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            answer.append(even_sum)
        
        return answer 
        



        