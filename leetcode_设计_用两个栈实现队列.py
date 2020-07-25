class CQueue:

    def __init__(self):
        self.stackpush = []
        self.stackpop = []

    def appendTail(self, value: int) -> None:
        self.stackpush.append(value)

    def deleteHead(self) -> int:
        if len(self.stackpop) == 0:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())
        if len(self.stackpop)==0:
            ans=-1
        else:
            ans=self.stackpop.pop()
        return ans