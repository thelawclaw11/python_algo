from collections import deque

class MyQueue:

    def __init__(self):
        self.left_stack = deque()
        self.right_stack = deque()

    def push(self, x: int) -> None:
        self.left_stack.appendleft(x)

    def pop(self) -> int:

        while len(self.left_stack) > 0:
            self.right_stack.appendleft(self.left_stack.popleft())

        popped = self.right_stack.popleft()

        while len(self.right_stack) > 0:
            self.left_stack.appendleft(self.right_stack.popleft())

        return popped

    def peek(self) -> int:

        while len(self.left_stack) > 0:
            self.right_stack.appendleft(self.left_stack.popleft())

        top = self.right_stack[0]

        while len(self.right_stack) > 0:
            self.left_stack.appendleft(self.right_stack.popleft())

        return top

    def empty(self) -> bool:
        return len(self.left_stack) == 0

queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print(queue.pop())
print(queue.left_stack)
print(queue.pop())
print(queue.left_stack)
print(queue.pop())
print(queue.left_stack)
print(queue.pop())
print(queue.left_stack)

