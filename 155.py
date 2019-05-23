class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        if self.minstack == [] or x < self.getMin():
            self.minstack.append(x)
        else:
            self.minstack.append(self.getMin())

    def pop(self) -> 'None':
        if self.stack == []:
            return
        else:
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> 'int':
        return self.stack[-1]

    def getMin(self) -> 'int':
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()