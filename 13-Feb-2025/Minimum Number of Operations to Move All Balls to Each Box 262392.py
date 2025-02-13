# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        ans = [0] * n

        balls_left, balls_right, move_left, move_right = 0, 0, 0, 0
        for i in range(n):

            ans[i] += move_left
            balls_left += int(boxes[i])
            move_left += balls_left

            j = n - 1 - i

            ans[j] += move_right
            balls_right += int(boxes[j])
            move_right += balls_right
            
        return ans
        