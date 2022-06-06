from collections import defaultdict
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:

        result = 0
        flavors_count = defaultdict(int)

        for candy in candies:
            flavors_count[candy] += 1

        if k == 0:
            return len(flavors_count)

        def remove(index):
            nonlocal flavors_count
            flavors_count[candies[index]] -= 1
            if flavors_count[candies[index]] == 0:
                del flavors_count[candies[index]]

        for right in range(k):
            remove(right)

        result = max(result, len(flavors_count))

        for right in range(k, len(candies)):
            remove(right)

            left = right - k
            flavors_count[candies[left]] += 1
            result = max(result, len(flavors_count))

        return result

solution = Solution()
print(solution.shareCandies([6,2,2,2], 2))