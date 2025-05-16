# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        counts = []
        
        def dfs(node: TreeNode, level: int):
            if not node:
                return
            if level == len(sums):
                sums.append(0)
                counts.append(0)
            sums[level] += node.val
            counts[level] += 1
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return [s / c for s, c in zip(sums, counts)]