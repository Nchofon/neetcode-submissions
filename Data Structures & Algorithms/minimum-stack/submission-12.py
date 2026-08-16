class MinStack:

    def __init__(self):
        self.myStack = []
        self.myMin = []

    def push(self, val: int) -> None:
        self.myStack.append(val)
        if self.myMin == [] or val <= self.myMin[-1]:
            self.myMin.append(val)
        
    def pop(self) -> None:
        if self.myStack[-1] == self.myMin[-1] :
            self.myMin.pop()
        self.myStack.pop()
        

    def top(self) -> int:
        return self.myStack[-1] if self.myStack[-1] else 0
        

    def getMin(self) -> int:
        return self.myMin[-1]
        
