from collections import deque

class Solution:
    def calPoints(self, ops):
        stack = deque()

        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))