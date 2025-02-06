# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment_open = False
        ans = []

        for line in source:
            i = 0

            if not comment_open:
                new_line = []
            while i < len(line):
                if line[i : i + 2] == "/*" and not comment_open:
                    comment_open = True
                    i += 1
                elif line[i : i + 2] == "*/" and comment_open:
                    comment_open = False
                    i += 1
                elif line[i : i + 2] == "//" and not comment_open:
                    break
                elif not comment_open:
                    new_line.append(line[i])
                
                i += 1
            if new_line and not comment_open:
                ans.append("".join(new_line))
        
        return ans