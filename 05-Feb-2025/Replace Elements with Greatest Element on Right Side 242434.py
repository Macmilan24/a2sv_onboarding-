# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_num

            if temp > max_num:
                max_num = temp
        
        return arr
        
            
        