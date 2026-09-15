class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = {}

    def push(self, val: int) -> None:
        length = len(self.stack)
        if length == 0:
            self.minimum[0] = val
        else:
            self.minimum[length] = min(val, self.minimum[length - 1])
        self.stack.append(val)

    def pop(self) -> None:
        self.minimum.pop(len(self.stack) - 1)
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minimum[len(self.stack) - 1]
