# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            
        n = len(arr)
        res = []

        for i in range(n - 1, -1 , -1):
            max_ind = i

            for j in range(i, -1, -1):
                if arr[j] > arr[max_ind]:
                    max_ind = j
            
            if max_ind != i:
                flip(max_ind)
                flip(i)
                res.append(max_ind + 1)
                res.append(i + 1)
        
        return res
            
