# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        in_stack = set()

        for c in s:
            counter[c] -= 1
            if c in in_stack:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)