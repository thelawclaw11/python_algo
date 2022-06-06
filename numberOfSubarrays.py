from typing import List

def is_odd(n):
    return n % 2 != 0

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = []

        for i in range(len(nums)):
            if is_odd(nums[i]):
                odds.append(i)

        result = 0

        for l in range(len(odds) - k + 1):
            r = l + k - 1
            next_r_value = odds[r + 1] if r + 1 < len(odds) else len(nums)
            previous_l_value = odds[l - 1] if l - 1 >= 0 else - 1

            result += (odds[l] - previous_l_value) * (next_r_value - odds[r])

        return result

solution = Solution()

#11
# print(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2,1,2,1], 3))

#16
print(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))