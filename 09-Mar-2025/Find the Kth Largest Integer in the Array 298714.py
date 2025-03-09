# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        numbers = sorted([int(num) for num in nums], reverse=True)
        return str(numbers[k-1])