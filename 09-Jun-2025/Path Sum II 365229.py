# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        
        def dfs(node: Optional[TreeNode], remaining_sum: int, path: List[int]):
            
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and remaining_sum == node.val:
                results.append(list(path))
            
            dfs(node.left, remaining_sum - node.val, path)
            dfs(node.right, remaining_sum - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        
        return results