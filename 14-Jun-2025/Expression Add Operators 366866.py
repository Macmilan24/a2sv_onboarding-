# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []
        n = len(num)

        def backtrack(pos, expr, evaluated, last):
            if pos == n:
                if evaluated == target:
                    res.append("".join(expr))
                return

            for i in range(pos, n):
                if i != pos and num[pos] == '0':
                    break

                curr_str = num[pos:i+1]
                curr = int(curr_str)

                if pos == 0:

                    backtrack(i + 1, [curr_str], curr, curr)
                else:

                    backtrack(i + 1, expr + ['+', curr_str], evaluated + curr, curr)
                    backtrack(i + 1, expr + ['-', curr_str], evaluated - curr, -curr)
                    backtrack(i + 1, expr + ['*', curr_str], evaluated - last + last * curr, last * curr)

        backtrack(0, [], 0, 0)
        return res