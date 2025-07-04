# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path = []
        dest_path = []

        def dfs(cur_node, path):
            if not cur_node:
                return
            
            if cur_node.val == startValue:
                start_path[:] = path[:]
            if cur_node.val == destValue:
                dest_path[:] = path[:]
            
            path.append("L")
            dfs(cur_node.left, path)
            path.pop()

            path.append("R")
            dfs(cur_node.right, path)
            path.pop()
            
        
        dfs(root,[])

        i = 0
        while i < len(start_path) and i < len(dest_path):
            if start_path[i] != dest_path[i]:
                break
            i += 1

        up_moves = "U" * (len(start_path) - i)
        down_moves = "".join(dest_path[i:])

        return up_moves + down_moves    
        
