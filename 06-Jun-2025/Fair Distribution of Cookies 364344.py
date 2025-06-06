# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        buckets = [0] * k

        def backtrack(i):
            nonlocal res
            if i == len(cookies):
                res = min(res, max(buckets))
                return
            if res <= max(buckets):  
                return
            for j in range(k):
                buckets[j] += cookies[i]
                backtrack(i + 1)
                buckets[j] -= cookies[i]
                if buckets[j] == 0:
                    break 

        backtrack(0)
        return res