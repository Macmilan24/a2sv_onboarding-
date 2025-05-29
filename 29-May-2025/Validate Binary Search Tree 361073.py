# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, minVal=float('-inf'), maxVal=float('inf')):
            if not node:
                return True
            if not (minVal < node.val < maxVal):
                return False
            return (
                helper(node.left, minVal, node.val) and
                helper(node.right, node.val, maxVal)
            )
        
        return helper(root)