# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        river = -1
        step = 0
        inital_capacity = capacity

        for i in range(len(plants)):
            if plants[i] > capacity:
                capacity = inital_capacity
                step += 2*i + 1
            else:
                step += 1
            capacity -= plants[i]
        
        return step
        