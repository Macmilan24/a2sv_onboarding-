# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def rev_bubble_sort(arr):

            for i in range(len(arr)):
                for j in range(0, len(arr) - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            return arr
        
        hash_map = {}
        ans = []

        for i in range(len(names)):
            hash_map[heights[i]] = names[i]
        
        heights = rev_bubble_sort(heights)

        for height in heights:
            ans.append(hash_map[height])
        
        return ans
        