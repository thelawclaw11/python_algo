class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        table = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        nums = []

        for char in word:
            nums.append(table[char])

        print(nums)

        ones = []

        for index, n in enumerate(nums):
            if n == 1:
                ones.append(index)
        best = 0

        farthest_traveled = 0

        for left in ones:
            if left < farthest_traveled:
                continue
            right = left + 1
            current_nums = {1}

            while right < len(nums) and nums[right] >= nums[right - 1] and \
                    (nums[right] == 1 or nums[right] - 1 in current_nums):
                current_nums.add(nums[right])
                right += 1

            farthest_traveled = right

            if len(current_nums) == 5:
                best = max(best, right - left)

        return best

solution = Solution()
# print(solution.longestBeautifulSubstring("aeiou"))
print(solution.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))


