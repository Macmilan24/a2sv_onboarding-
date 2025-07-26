# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        
        def bfs(node: TreeNode, path: str):
            if not path:
                path = str(node.val)
            else:
                path += "->" + str(node.val)
                
            if not node.left and not node.right:
                result.append(path)
                return
            
            if node.left:
                bfs(node.left, path)
            if node.right:
                bfs(node.right, path)
        
        bfs(root, "")
        return result