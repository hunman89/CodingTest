class MyQueue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack.pop()

    def peek(self) -> int:
        self.move()
        return self.stack[-1]

    def empty(self) -> bool:
        return True if (len(self.queue) is 0) and (len(self.stack) is 0) else False

    def move(self):
        if len(self.stack) is 0:
            while len(self.queue) is not 0:
                self.stack.append(self.queue.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()