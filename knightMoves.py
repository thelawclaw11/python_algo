from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        q = deque([(0, 0)])

        visited = set()

        moves = 0

        while q:
            n = len(q)

            for _ in range(n):
                curr_x, curr_y = q.pop()

                if (curr_x,curr_y) in visited:
                    continue

                visited.add((curr_x,curr_y))

                if (curr_x,curr_y) == (x,y):
                    return moves

                for offset_x, offset_y in offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y

                    if (next_x, next_y) not in visited:
                        visited.add((next_x,next_y))
            moves += 1

solution = Solution()

print(solution.minKnightMoves(3,3))
r