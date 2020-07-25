class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mystack=[]
        self.minstack=[]

    def push(self, x: int) -> None:
        self.mystack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        elif self.minstack[-1]<x:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(x)

    def pop(self) -> None:
        self.mystack=self.mystack[:-1]
        self.minstack=self.minstack[:-1]

    def top(self) -> int:
        if self.mystack:
            return self.mystack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


if __name__=="__main__":
    minStack=MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()

    minStack.pop()
    minStack.top()

    minStack.getMin()
