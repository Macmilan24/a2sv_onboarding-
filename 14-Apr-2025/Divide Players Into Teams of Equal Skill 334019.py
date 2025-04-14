# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_sum = sum(skill)
        teams = n // 2

        if total_sum * 2 % n != 0:
            return -1
        
        target = (total_sum * 2) // n
        skill.sort()
        chemistry = 0
        
        for i in range(teams):
            a = skill[i]
            b = skill[n - 1 - i]
            if a + b != target:
                return -1
            chemistry += a * b
            
        return chemistry