from collections import deque
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, best, zeros = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while left <= right and zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        

        return best

solution = Solution()

# 6
print(solution.longestOnes([0,0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

# 6
# print(solution.longestOnes([0,0,1,1,0,0,1], 3))

# 3
# print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1], 0))

# print(solution.longestOnes([0,1,1,0,0,1,1,1,0,1,1], 3))
# print(solution.longestOnes([0,0,1,1,1,0,0], 0))
