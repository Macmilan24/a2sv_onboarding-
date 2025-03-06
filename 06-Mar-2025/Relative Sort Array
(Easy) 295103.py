# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = {}
        end = []
        for num in arr1:
            if num not in arr2:
                end.append(num)
            arr1_count[num] = arr1_count.get(num, 0) + 1
        
        end.sort()
        res = []

        for num in arr2:
            for _ in range(arr1_count[num]):
                res.append(num)
        
        return res + end


            

