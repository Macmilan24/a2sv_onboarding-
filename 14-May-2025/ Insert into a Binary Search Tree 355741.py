# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root

        while cur:
            par = cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        
        if par.val > val:
            par.left = TreeNode(val)
        else:
            par.right = TreeNode(val)
        
        return root