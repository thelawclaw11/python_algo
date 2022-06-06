from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        best = 0

        left = 0

        table = defaultdict(int)

        for right in range(len(s)):
            table[s[right]] += 1

            while len(table) > k:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1

            best = max(best, right - left + 1)
        return best


solution = Solution()
print(solution.lengthOfLongestSubstringKDistinct("eceba", 2))