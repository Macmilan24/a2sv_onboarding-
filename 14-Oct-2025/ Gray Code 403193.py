# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        prev = self.grayCode(n - 1)
        add_on = 1 << (n - 1)
        
        return prev + [add_on + x for x in reversed(prev)]