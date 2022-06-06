from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        table_of_substrings = defaultdict(int)

        chars = defaultdict(int)

        left = 0
        for right in range(len(s)):
            chars[s[right]] += 1

            while left < right and (
                    len(chars) > maxLetters or right - left + 1 > maxSize):
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1

            if len(chars) <= maxLetters and right - left + 1 >= minSize and right - left + 1 <= maxSize:
                table_of_substrings[s[left:right + 1]] += 1

        print(table_of_substrings)

        return max(table_of_substrings.values())


solution = Solution()

# print(solution.maxFreq("aababcaab", 2, 3, 4))
print(solution.maxFreq("aabcabcab", 2, 2, 3))
