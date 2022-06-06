import math
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = 0

        for n in data:
            if n == 1:
                ones_count += 1

        counts = {1: 0, 0: 0}

        L = 0
        smallest = math.inf

        for R in range(len(data)):
            counts[data[R]] += 1

            if R - L + 1 > ones_count:
                counts[data[L]] -= 1
                L += 1

            if ones_count - counts[1] == counts[0]:
                smallest = min(smallest, counts[0])
        return smallest



solution = Solution()
print(solution.minSwaps([1,0,1,0,0,1,1,0,1,0]))