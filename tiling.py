from functools import cache
from typing import NamedTuple

class Result(NamedTuple):
    full: int
    partial: int


class Solution:
    def numTilings(self, n: int) -> int:

        @cache
        def f(n) -> Result:
            if n == 1:
                return Result(1, 0)

            if n == 2:
                return Result(2, 2)

            full = f(n - 1).full + f(n - 2).full + f(n - 1).partial + f(n - 1).partial
            partial = f(n-2).full + f(n - 1).partial

            return Result(full, partial)

        return f(n).full

solution = Solution()
print(solution.numTilings(10))

def tile(n, tiles):

    @cache
    def b(k):

        if k == 0:
            return 1

        if k < 0:
            return 0

        return sum([b(k - t) for t in tiles])

    return b(n)

print(tile(7, [1,1,1,1,1,1,2,4,5]))
