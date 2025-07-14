# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])

        start_x, start_y = entrance
        queue = deque()
        distance = [[float("inf")] * col for _ in range(row)]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def in_bound(x, y, dis):
            if 0 <= x < row and 0 <= y < col and maze[x][y] != "+" and distance[x][y] == float("inf"):
                return True
            else:
                return False   

        distance[start_x][start_y] = 0
        queue.append((start_x, start_y, 0))

        while len(queue) > 0:
            x, y, dis = queue.popleft()

            if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                if not (x == start_x and y == start_y):
                    return dis
            
            for dx, dy in directions:
                new_x = dx + x
                new_y = y + dy

                if in_bound(new_x, new_y, dis):
                    distance[new_x][new_y] = dis + 1
                    queue.append((new_x, new_y, dis + 1))
        
        return - 1

