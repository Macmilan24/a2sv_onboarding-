# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_path = defaultdict(list)
        blue_path = defaultdict(list)

        for a, b in redEdges:
            red_path[a].append(b)
        for u, v in blueEdges:
            blue_path[u].append(v)

        
        distance = [[float('inf')] * 2 for _ in range(n)] # distance[node][color]
        distance[0][0] = 0
        distance[0][1] = 0

        visited = set()
        queue = deque([(0,0), (0, 1)])

        while queue:
            node, color = queue.popleft()
            nxt_color = 1 if color == 0 else 0

            neighbors = blue_path[node] if nxt_color == 1 else red_path[node]
        
            for neighbor in neighbors:
                new_dist = distance[node][color] + 1
                if new_dist < distance[neighbor][nxt_color]:
                    distance[neighbor][nxt_color] = new_dist
                    if (neighbor, nxt_color) not in visited:
                        queue.append((neighbor, nxt_color))
                        visited.add((neighbor, nxt_color))
        
        answer = [0] * n
        for i in range(n):
            answer[i] = min(distance[i][0], distance[i][1])
            if answer[i] == float('inf'):
                answer[i] = -1
        
        return answer

