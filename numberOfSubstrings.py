from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {x: 0 for x in "abc"}
        out, l = 0, 0

        for r in range(len(s)):
            counter[s[r]] += 1
            while all(counter.values()):
                out += len(s) - r
                counter[s[l]] -= 1
                l += 1
        return out

solution = Solution()

# print(solution.numberOfSubstrings("abcabc"))

# 20
print(solution.numberOfSubstrings("aaaccbabc"))

# 10
# print(solution.numberOfSubstrings("abcabc"))