# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_char = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[char] <= char_count[char] for char in word_count):
                total_char += len(word)
        
        return total_char