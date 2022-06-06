from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sums = []

        for n in nums:
            prev_sum = prefix_sums[-1] if len(prefix_sums) > 0 else 0
            prefix_sums.append(prev_sum + n)

        def get_sum(start, end):
            return prefix_sums[end] - (prefix_sums[start - 1] if start > 0 else 0)




solution = Solution()
print(solution.maxSubArrayLen([1,-1,5,-2,3], 3))