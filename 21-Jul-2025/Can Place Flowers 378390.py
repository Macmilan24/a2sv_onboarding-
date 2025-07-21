# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        i = 0
        
        while i < length:
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i-1] == 0)
                next_empty = (i == length-1 or flowerbed[i+1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    i += 2 
                else:
                    i += 1
            else:
                i += 2
            if count >= n:
                return True
                
        return count >= n