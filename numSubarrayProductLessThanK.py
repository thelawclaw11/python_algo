from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0

        left = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]

            while left < right and product >= k:
                product /= nums[left]
                left += 1

            if product < k:
                count += right - left + 1

        return count


solution = Solution()
print(solution.numSubarrayProductLessThanK([10, 5, 2, 6, 1], 100))
