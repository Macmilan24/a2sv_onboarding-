# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pathSum):
            if node is None:
                return 0

            newSum = pathSum * 10 + node.val

            if node.left is None and node.right is None:
                return newSum

            leftSum = dfs(node.left, newSum)
            rightSum = dfs(node.right, newSum)

            total = leftSum + rightSum
            return total

        result = dfs(root, 0)
        return result