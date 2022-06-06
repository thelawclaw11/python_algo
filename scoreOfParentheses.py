from collections import namedtuple

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()


    def scoreOfParentheses1(self, s: str) -> int:
        stack = list()
        sums_table = dict()
        current_level = -1

        for char in s:
            if char == "(":
                stack.append(current_level)
                current_level += 1
            elif char == ")":
                if current_level not in sums_table:
                    sums_table[current_level] = 0

                if current_level + 1 in sums_table:
                    sums_table[current_level] += 2 * sums_table[current_level + 1]
                    del sums_table[current_level + 1]
                else:
                    sums_table[current_level] += 1

                current_level -= 1
        return sums_table[0]





solution = Solution()

# 1
print(solution.scoreOfParentheses("()"))

# # 2
print(solution.scoreOfParentheses("()()"))
#
# # 2
print(solution.scoreOfParentheses("(())"))
#
# # 4
print(solution.scoreOfParentheses("(()())"))
#
# # 8
print(solution.scoreOfParentheses("(((())))"))
#
# # 10
print(solution.scoreOfParentheses("(()(()()))"))