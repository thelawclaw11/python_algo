from typing import List

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        sums = []

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                sums.append(current_sum)

        sums.sort()

        print(sums)

        return sums[k - 1]

solution = Solution()

print(solution.kthSmallestSubarraySum([3,3,5,5], 7))