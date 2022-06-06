from typing import List

from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        k_is_even = k % 2 == 0

        left = 0

        bigs = SortedList()
        smalls = SortedList()

        def balance():
            nonlocal bigs, smalls

            if len(bigs) == len(smalls):
                pass

            elif len(bigs) > len(smalls):
                smalls.add(bigs.pop(0))

            elif len(smalls) > len(bigs) + 1:
                bigs.add(smalls.pop(-1))

        result = []

        for right in range(len(nums)):
            if smalls and nums[right] > smalls[-1]:
                bigs.add(nums[right])
            else:
                smalls.add(nums[right])

            balance()

            if right - left == k:
                to_remove = nums[left]
                if to_remove in bigs:
                    bigs.discard(to_remove)

                elif to_remove in smalls:
                    smalls.discard(to_remove)

                left += 1

            balance()

            if right - left == k - 1:
                if k_is_even:
                    result.append((bigs[0] + smalls[-1]) / 2)
                else:
                    result.append(smalls[-1])

        return result

sol = Solution()

print(sol.medianSlidingWindow([5,5,8,1,4,7,1,3,8,4], 8))