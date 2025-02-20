# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        boomerangs = 0

        for i in range(len(points)):
            distance_map = {}

            for j in range(len(points)):
                if i == j:
                    continue
                
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distance = dx**2 + dy**2  #Euclidean distance with out sqrt

                distance_map[distance] = distance_map.get(distance, 0) + 1
            
            for count in distance_map.values():
                if count > 1:
                    boomerangs += count * (count - 1)
        
        return boomerangs