import math
from typing import List


class Solution:
    def maxScore(self, all_cards: List[int], k: int) -> int:
        prefix_sums = []

        for n in all_cards:
            prev_sum = prefix_sums[-1] if len(prefix_sums) > 0 else 0
            prefix_sums.append(prev_sum + n)

        def get_sum(start, end):
            return prefix_sums[end] - (prefix_sums[start - 1] if start > 0 else 0)

        length = len(all_cards)

        best = 0

        best = max(best, get_sum(0, k - 1), get_sum(length - k, length - 1))

        L = k - 2
        R = length - 1

        while L > -1:
            right_sum = get_sum(R, length - 1)
            left_sum = get_sum(0, L)

            best = max(best, right_sum + left_sum)

            L -= 1
            R -= 1

        return best







solution = Solution()
# 12
# print(solution.maxScore([1,2,3,4,5],3))
# 12
print(solution.maxScore([1,2,3,4,5,6,1], 3))
# 490
# print(solution.maxScore([61,16,51,40,37,21,96,70,13,98],9))