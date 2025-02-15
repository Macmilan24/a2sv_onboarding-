# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch (self, arr, tar):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (right + left) // 2

                if arr[mid] == tar:
                    return True
                elif arr[mid] < tar:
                    left = mid + 1
                elif arr[mid] > tar:
                    right = mid - 1
            
            return False
        
        for arr in matrix:
            if binarySearch(self,arr, target):
                return True
        return False

        