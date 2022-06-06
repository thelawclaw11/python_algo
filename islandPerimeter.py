from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        visited = [[False for j in range(cols)] for i in range(rows)]

        start_row = None
        start_col = None

        for row in range(rows):
            if start_row is not None:
                break
            for col in range(cols):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
                    break

        def dfs(row, col):
            nonlocal result
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if grid[row][col] == 0:
                return

            if visited[row][col]:
                return

            visited[row][col] = True

            top = grid[row - 1][col] if row - 1 >= 0 else 0
            bottom = grid[row + 1][col] if row + 1 < rows else 0
            left = grid[row][col - 1] if col - 1 >= 0 else 0
            right = grid[row][col + 1] if col + 1 < cols else 0

            result += (4 - top - bottom - left - right)

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return

        dfs(start_row, start_col)

        return result


solution = Solution()

alpha = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(solution.islandPerimeter(alpha))
