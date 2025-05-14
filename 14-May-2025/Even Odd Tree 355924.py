# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        is_even = True
        queue = deque([root])

        while queue:
            prev = float("-inf") if is_even else float("inf")

            for _ in range(len(queue)):
                temp = queue.popleft()
                if is_even:
                    if temp.val % 2 == 0 or temp.val <= prev:
                        return False
                else:
                    if temp.val % 2 == 1 or temp.val >= prev:
                        return False
                
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
                
                prev = temp.val
            
            is_even = not is_even
        
        return True

