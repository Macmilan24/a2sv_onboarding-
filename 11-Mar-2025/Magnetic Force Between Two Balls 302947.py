# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def can_place_ball(pos, m, force):
            count = 1
            last_pos = pos[0]

            for i in range(1, len(pos)):
                cur_pos = pos[i]

                if cur_pos - last_pos >= force:
                    count += 1
                    last_pos = cur_pos
            
            return count >= m

        
        position.sort()
        
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_place_ball(position, m, mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result