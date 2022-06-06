from collections import deque

class Solution:
    def backspaceCompare(self, left: str, right: str) -> bool:
        left_stack = deque()

        for char in left:
            if char == "#":
                if len(left_stack) > 0:
                    left_stack.pop()
            else:
                left_stack.append(char)

        right_stack = deque()

        for char in right:
            if char == "#":
                if len(right_stack) > 0:
                    right_stack.pop()
            else:
                right_stack.append(char)

        return left_stack == right_stack

solution = Solution()

# true
print(solution.backspaceCompare("ab#c", "ad#c"))

# true
print(solution.backspaceCompare("ab##", "c#d#"))

# false
print(solution.backspaceCompare("a#c", "b"))

