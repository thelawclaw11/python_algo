from typing import List

ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: int(a / b),
    "*": lambda a, b: a * b
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def F(i):
            try:
                return int(tokens[i]), i
            except ValueError:
                pass
            # tokens[i] is operator

            right_value, right_index_end = F(i - 1)
            left_value, left_index_end = F(right_index_end - 1)

            root_value = ops[tokens[i]]



            return root_value, left_index_end

        return F(len(tokens) - 1)[0]

solution = Solution()

print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))