# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        min_move = 0
        for x, y in zip(sorted(seats), sorted(students)):
            min_move += abs(x - y)
        
        return min_move