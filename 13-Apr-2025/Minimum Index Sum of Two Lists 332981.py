# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                total_index = index_map[word] + j
                if total_index < min_sum:
                    min_sum = total_index
                    result = [word]
                elif total_index == min_sum:
                    result.append(word)

        return result