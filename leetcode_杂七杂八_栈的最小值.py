class Minstack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]


    def push(self,e):
        self.stack1.append(e)
        if len(self.stack2)==0 or e<self.stack2[-1]:
            self.stack2.append(e)
        else:
            self.stack2.append(self.stack2[-1])

    def pop(self):
        e=self.stack1.pop()
        self.stack2.pop()
        return e

    def getMin(self):
        return self.stack2[-1]

    def top(self):
        return self.stack1[-1]


if __name__=="__main__":
    minStack=Minstack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())