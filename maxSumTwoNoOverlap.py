import math
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sums = []

        for n in nums:
            prev_sum = prefix_sums[-1] if len(prefix_sums) > 0 else 0
            prefix_sums.append(prev_sum + n)

        def get_sum(start, end):
            return prefix_sums[end] - (prefix_sums[start - 1] if start > 0 else 0)

        largest_before_table = {}
        biggest = -math.inf

        for left in range(len(nums) - secondLen + 1):
            right = left + secondLen - 1
            window_sum = get_sum(left, right)
            temp_biggest = max(biggest, window_sum)
            largest_before_table[right + 1] = temp_biggest
            biggest = temp_biggest

        largest_after_table = {}
        biggest = -math.inf

        for right in range(len(nums) - 1, -1 + secondLen - 1, -1):
            left = right - secondLen + 1
            window_sum = get_sum(left, right)
            temp_biggest = max(biggest, window_sum)
            largest_after_table[left - 1] = temp_biggest
            biggest = temp_biggest

        best = -math.inf

        for first_window_start in range(len(nums) - firstLen + 1):
            first_window_end = first_window_start + firstLen - 1

            largest_before = largest_before_table[first_window_start] if first_window_start in largest_before_table else -math.inf
            largest_after = largest_after_table[first_window_end] if first_window_end in largest_after_table else -math.inf

            best = max(best, get_sum(first_window_start, first_window_end) + max(largest_after, largest_before))
        return best


solution = Solution()
# 95
# print(solution.maxSumTwoNoOverlap([4,5,14,16,16,20,7,13,8,15], 3, 5))
# 20
print(solution.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
