# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        k = len(p)
        p_count = Counter(p)
        window_count = Counter(s[:k])

        res = [0] if p_count == window_count else []

        for i in range(k, len(s)):
            window_count[s[i - k]] -= 1
            if window_count[s[i - k]] == 0:
                del window_count[s[i - k]]
            
            window_count[s[i]] =  window_count.get(s[i], 0) + 1

            if window_count == p_count:
                res.append(i - k + 1)
        
        return res


        