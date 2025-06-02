# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                helper(i, path,total + candidates[i])
                path.pop()
        
        helper(0, [], 0)
        return res