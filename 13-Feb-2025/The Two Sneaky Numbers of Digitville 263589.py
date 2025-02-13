# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_count = Counter(nums)
        sneaky_num = []
        for num in num_count:
            if num_count[num] >= 2:
                sneaky_num.append(num)
        
        return sneaky_num