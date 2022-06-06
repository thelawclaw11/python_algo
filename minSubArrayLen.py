import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        smallest = math.inf
        left = 0
        su = 0

        for right in range(len(nums)):
            su += nums[right]

            while su >= target:
                smallest = min(smallest, right - left + 1)
                su -= nums[left]
                left += 1

        if smallest == math.inf:
            return 0
        return smallest

solution = Solution()


print(solution.minSubArrayLen(11,[1,2,3,4,5]))