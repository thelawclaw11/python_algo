class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        left = 0
        non_B_count = 0
        for right in range(len(s)):
            if s[right] != "B":
                non_B_count += 1

            while left < right and non_B_count > k:
                if s[left] != "B":
                    non_B_count -= 1

                left += 1
            result = max(result, right - left + 1)

        return result

solution = Solution()
print(solution.characterReplacement("AABABBA", 1))