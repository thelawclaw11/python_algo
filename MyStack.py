from collections import deque

class MyStack:

    def __init__(self):
        self.left_queue = deque()
        self.right_queue = deque()

    def push(self, x: int) -> None:
        self.left_queue.appendleft(x)

    def pop(self) -> int:
        top = None
        while len(self.left_queue) > 0:
            if len(self.left_queue) == 1:
                top = self.left_queue[0]
                self.left_queue.pop()
            else:
                self.right_queue.appendleft(self.left_queue.pop())

        self.left_queue = self.right_queue
        self.right_queue = deque()

        return top

    def top(self) -> int:
        top = None
        while len(self.left_queue) > 0:
            if len(self.left_queue) == 1:
                top = self.left_queue[0]
            self.right_queue.appendleft(self.left_queue.pop())

        self.left_queue = self.right_queue
        self.right_queue = deque()

        return top

    def empty(self) -> bool:
        return len(self.left_queue) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.left_queue)
print(stack.pop())
print(stack.left_queue)
