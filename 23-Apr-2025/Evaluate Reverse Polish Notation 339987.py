# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token == "+":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                val = num2 + num1
                num_stack.append(val)
            elif token == "-":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                val = num2 - num1
                num_stack.append(val)
            elif token == "*":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                val = num2 * num1
                num_stack.append(val)
            elif token == "/":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                val = num2 / num1
                num_stack.append(int(val))
            else:
                num_stack.append(int(token))
        
        return num_stack[0]
        