from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffled = nums[:]

    def reset(self) -> List[int]:
        self.shuffled = self.nums
        return self.shuffled

    def shuffle(self) -> List[int]:
        cop = self.nums[:]
        out = []
        l = 0

        while cop:
            choice = randint(l, len(cop) - 1) if (l != len(cop) - 1) else l
            out.append(cop[choice])
            cop[l], cop[choice] = cop[choice], cop[l]
            l += 1

        self.shuffled = out

        return out

sol = Solution([1,2,3,4,5])
print(sol.shuffle())
