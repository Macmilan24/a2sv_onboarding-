# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

        