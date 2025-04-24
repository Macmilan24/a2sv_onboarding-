# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:

        path_list = path.split("/")
        stack = []
        
        for char in path_list:
            if char == "":
                continue
            
            if char == "..":
                if stack:
                    stack.pop()
            elif char == ".":
                continue
            else:
                stack.append(char)
        
        print(stack)
        
        return "/" + "/".join(stack)