import string
from collections import defaultdict


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        result = 0

        total_counts = defaultdict(lambda: 0)

        for char in text:
            total_counts[char] += 1

        for letter in string.ascii_lowercase:
            total_letter_count = total_counts[letter]

            left = 0
            bad_count = 0
            good_count = 0

            for right in range(len(text)):
                if text[right] == letter:
                    good_count += 1
                else:
                    bad_count += 1

                while left < right and bad_count > 1:
                    if text[left] == letter:
                        good_count -= 1
                    else:
                        bad_count -= 1

                    left += 1

                if total_letter_count - good_count >= 1 and bad_count == 1:
                    result = max(result, good_count + 1)
                else:
                    result = max(result, good_count)

        return result

solution = Solution()

print(solution.maxRepOpt1("aaabbaaa"))