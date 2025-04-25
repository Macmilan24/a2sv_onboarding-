# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
        

    def push(self, val: int) -> None:
        self.min_val = self.getMin()

        if self.min_val == None or self.min_val > val:
            self.min_val = val
        
        self.stack.append((val, self.min_val))

    def pop(self) -> None:

        self.stack.pop()

    def top(self) -> int:

        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:

        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()