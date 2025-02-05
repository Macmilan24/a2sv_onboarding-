# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length_ = len(arr)
        i = 0
    
        while i+1 < length_ and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == length_ - 1:
            return False
    
        while i+1 < length_ and arr[i] > arr[i+1]:
            i += 1
        
        return i == length_ - 1
        

                 