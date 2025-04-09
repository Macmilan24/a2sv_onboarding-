# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        n = len(word)
        
        for i in range(n):
            curr_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                curr_vowels.add(word[j])
                if len(curr_vowels) == 5:
                    count += 1
                    
        return count