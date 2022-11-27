import copy
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        nums = set(str(n) for n in range(1, 10))

        rows = {n: set() for n in range(9)}
        cols = {n: set() for n in range(9)}
        squares = {}

        for row in range(3):
            for col in range(3):
                squares[(row, col)] = set()

        for row in range(9):
            for col in range(9):
                cur = board[row][col]

                if cur == ".":
                    continue

                rows[row].add(cur)
                cols[col].add(cur)
                squares[(row // 3, col // 3)].add(cur)

        print(rows)
        print(cols)
        print(squares)

        seen = set()
        answer = None

        def backtrack(row, col):
            print(len(seen))
            nonlocal answer

            if (row, col) in seen:
                return

            if row < 0 or row >= 9 or col < 0 or col >= 9:
                return

            seen.add((row, col))

            if board[row][col] != ".":
                backtrack(row + 1, col)
                backtrack(row - 1, col)
                backtrack(row, col - 1)
                backtrack(row, col + 1)

            options = nums - (rows[row] | cols[col] | squares[(row // 3, col // 3)])

            for k in options:
                rows[row].add(k)
                cols[col].add(k)
                squares[(row // 3, col // 3)].add(k)
                board[row][col] = k

                backtrack(row + 1, col)
                backtrack(row - 1, col)
                backtrack(row, col - 1)
                backtrack(row, col + 1)

                if len(seen) == 81:
                    answer = copy.deepcopy(board)
                    return

                seen.discard((row, col))
                board[row][col] = "."
                rows[row].discard(k)
                cols[col].discard(k)
                squares[(row // 3, col // 3)].discard(k)

            return

        backtrack(0, 0)

        return answer


solution = Solution()

print(solution.solveSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
