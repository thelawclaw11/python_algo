from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        current = set()
        is_free = False

        def F(row, col):
            nonlocal current, is_free
            if (row, col) in current or row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == "X":
                return

            current.add((row, col))

            is_free = is_free or row == rows - 1 or row == 0 or col == cols - 1 or col == 0

            F(row + 1, col)
            F(row - 1, col)
            F(row, col + 1)
            F(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                current = set()
                is_free = False
                if board[row][col] == "O":
                    F(row, col)
                    if not is_free:
                        for r, c in current:
                            board[r][c] = "X"


solution = Solution()

input = [
    ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
    ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
    ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
    ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
    ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
    ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"]]

solution.solve(input)

print(input)

expected = [["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X"],["O","X","X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","O","O","X","X","O","X","X","O","O"]]