# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        j = 0
        radius = 0
        
        for house in houses:
            min_dis = float("inf")

            if j < len(heaters):
                min_dis = abs(house - heaters[j])
            while j < len(heaters) - 1 and abs(house - heaters[j + 1]) <= min_dis:
                j += 1
                min_dis = abs(house - heaters[j])
            
            radius = max(radius, min_dis)
        
        return radius
