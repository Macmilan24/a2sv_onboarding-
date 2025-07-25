# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)  
        indegree = {}              
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            ing_list = ingredients[i]
            indegree[recipe] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(recipe)

        queue = deque(supplies)  
        result = []

        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1 
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)

        return result