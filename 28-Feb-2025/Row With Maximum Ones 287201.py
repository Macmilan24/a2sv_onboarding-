# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0
        max_index = 0

        for i, row in enumerate(mat):
            count = row.count(1)
            if count > max_count:
                max_count = count
                max_index = i
        
        return [max_index, max_count]


        