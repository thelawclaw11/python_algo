from collections import deque

class Solution:
    def makeGood(self, s: str):
        stack = deque()

        # difference between uppercase and lowercase is 32

        for char in s:
            if len(stack) > 0 and abs(ord(char) - ord(stack[0])) == 32:
                stack.popleft()
            else:
                stack.appendleft(char)

        result = ""

        while len(stack) > 0:
            result += stack.pop()

        return result

solution = Solution()
# print(solution.makeGood("abBAcC"))
print(solution.makeGood("leEeetcode"))
