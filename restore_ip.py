from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def traverse(row, col):
            if (row, col) in visited or row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 0:
                return

            visited.add((row, col))

            traverse(row + 1, col)
            traverse(row - 1, col)
            traverse(row, col - 1)
            traverse(row, col + 1)

        for i in range(cols):
            traverse(0, i)
            traverse(rows - 1, i)

        for j in range(rows):
            traverse(j, 0)
            traverse(j, cols - 1)

        print(visited)

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    result += 1
                    traverse(r, c)

        return result

solution = Solution()

a = [
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1]]

print(solution.closedIsland(a))
