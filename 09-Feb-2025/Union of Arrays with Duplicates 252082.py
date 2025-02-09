# Problem: Union of Arrays with Duplicates - https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for i in range(left, right + 1):
            if not any(l <= i <= r for l, r in ranges):
                return False
        
        return True
                    

        