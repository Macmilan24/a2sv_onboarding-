# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split(" ")
        ans = []
        
        for i in range(len(res) - 1, -1, -1):
            if res[i] == "":
                continue
            ans.append(res[i])
        
        return " ".join(ans)