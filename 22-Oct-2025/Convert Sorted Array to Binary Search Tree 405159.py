# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            
            return root

        return build_tree(0, len(nums) - 1)