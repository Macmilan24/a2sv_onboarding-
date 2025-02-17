# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_count = Counter(word)
        freq = []

        for val in word_count.values():
            freq.append(val)

        for i in range(len(freq)):
            freq[i] -= 1

            if len(set(freq)) == 1:
                return True
            if freq[i] == 0:
                if len(set(freq)) == 2:
                    return True

            freq[i] += 1
        
        return False
