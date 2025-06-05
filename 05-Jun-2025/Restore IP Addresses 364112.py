# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(i = 0, no_dot = 0, cur = ""):
            if no_dot == 4 and i == len(s):
                result.append(cur[:-1])
                return
            
            if no_dot > 4:
                return

            limit = min(i + 3, len(s)) 
            for j in range(i, limit ):

                if int(s[i:j+1]) < 256:
                    if (i == j or s[i] != "0"):
                        backtrack(j + 1, no_dot + 1, cur + s[i:j + 1] + ".")
        
        backtrack()
        return result
