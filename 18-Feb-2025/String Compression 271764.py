# Problem: String Compression - https://leetcode.com/problems/string-compression/

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        fast = 0
        ans = []

        while fast < len(chars):
            count = 0
            
            while fast < len(chars) and chars[fast] == chars[slow]:
                count += 1
                fast += 1

            ans.append(chars[slow])
            if count > 1:
                ans.extend(str(count))
            
            slow = fast

        chars[:] = ans
        
        return len(chars)
