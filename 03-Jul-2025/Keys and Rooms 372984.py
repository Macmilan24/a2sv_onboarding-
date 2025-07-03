# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        queue = deque([0])
        visited.add(0)

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == n