class Solution:
    def isHappy(self, n: int) -> bool:
        nums_seen_before = set()

        number = n

        while number != 1:
            if number in nums_seen_before:
                return False
            else:
                nums_seen_before.add(number)
            digits = list(str(number))
            number = sum([int(d) ** 2 for d in digits])

        return True

solution = Solution()

print(solution.isHappy(2))