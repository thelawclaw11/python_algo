from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            chunks = []

            current_chunk = []
            for n in nums:
                if n == 1:
                    if current_chunk:
                        chunks.append(current_chunk)
                        current_chunk = []
                else:
                    current_chunk.append(n)

            if current_chunk:
                chunks.append(current_chunk)

            result = 0

            print(chunks)

            for chunk in chunks:
                n = len(chunk)
                result += (n * (n + 1))/2

            return int(result)

        ones = [-1]

        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i)

        ones.append(len(nums))

        result = 0

        for right in range(1 + goal - 1, len(ones) - 1):
            left = right - goal + 1

            left_side = ones[left] - ones[left - 1]
            right_side = ones[right + 1] - ones[right]

            result += left_side * right_side

        return result







solution = Solution()

# 67
print(solution.numSubarraysWithSum([1,0,0,1,0,0,1], 0))

# 20
# print(solution.numSubarraysWithSum([0,0,0,1,0,1,0,0,0,0], 2))

# print(solution.numSubarraysWithSum([0,0,0,0,0], 0))
# print(solution.numSubarraysWithSum([0,1,1,1,1], 3))