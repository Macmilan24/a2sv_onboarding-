# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        res = []

        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        for ans in anagrams.values():
            res.append(ans)
        
        return res
        
        