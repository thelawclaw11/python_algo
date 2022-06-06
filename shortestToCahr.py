import math
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [math.inf] * len(s)

        prev = math.inf

        for i in range(len(s)):
            if s[i] == c:
                prev = i

            result[i] = abs(i - prev)

        after = math.inf

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                after = i

            print(after, i)

            result[i] = min(result[i], abs(after - i))

        return result

solution = Solution()

print(solution.shortestToChar("loveleetcode", "e"))