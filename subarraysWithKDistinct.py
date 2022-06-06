from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        count = 0

        table = defaultdict(int)

        left = 0

        for right in range(len(nums)):
            table[nums[right]] += 1

            if len(table) == k and (right == len(nums) - 1 or nums[right + 1] not in table):
                while left < right and len(table) > k - 1:
                    count += 1
                    table[nums[left]] -= 1
                    if table[nums[left]] == 0:
                        del table[nums[left]]

                    left += 1

        return count

solution = Solution()
print(solution.subarraysWithKDistinct([1,2,1,3], 3))