# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        dirc = 0
        max_dis = 0

        obstacle = {tuple(o) for o in obstacles}

        for command in commands:
            if command == -1:
                dirc = (dirc + 1) % 4
            elif command == -2:
                dirc = (dirc - 1) % 4
            else:
                dx, dy = direction[dirc]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacle:
                        break
                    x, y = x + dx, y + dy
            
            max_dis = max(max_dis, x**2 + y**2)
        
        return max_dis

        