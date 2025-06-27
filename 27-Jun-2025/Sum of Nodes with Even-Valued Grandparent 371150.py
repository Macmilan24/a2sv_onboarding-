# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur_root, parent, grandparent):
            if cur_root == None:
                return 0
            
            res = 0
            
            if grandparent and grandparent.val % 2 == 0:
                res += cur_root.val
            
            return res + dfs(cur_root.left, cur_root, parent) + dfs(cur_root.right, cur_root, parent)
        
        return dfs(root, None, None)