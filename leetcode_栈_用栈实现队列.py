class MyQueue:

    def __init__(self):
        self.stackpush = []
        self.stackpop = []

    def push(self, x: int) -> None:
        self.stackpush.append(x)

    def pop(self) -> int:
        if len(self.stackpop) == 0:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())
        return self.stackpop.pop()

    def peek(self) -> int:
        if len(self.stackpop) == 0:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())
        return self.stackpop[-1]

    def empty(self) -> bool:
        return len(self.stackpop) == 0 and len(self.stackpush) == 0