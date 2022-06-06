from collections import defaultdict

class Solution:
    def countGoodSubstrings1(self, s: str) -> int:
        result = 0

        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                result += 1

        return result

    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        table = defaultdict(int)

        if len(s) < 3:
            return 0
        else:
            table[s[0]] += 1
            table[s[1]] += 1

        for i in range(2, len(s)):
            table[s[i]] += 1

            all_good = True

            for key in table:
                if table[key] != 1:
                    all_good = False
                    break

            if all_good:
                result += 1

            table[s[i - 2]] -= 1
            if table[s[i - 2]] == 0:
                del table[s[i - 2]]

        return result

solution = Solution()

alpha = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"


beta = alpha
print(beta)

print(solution.countGoodSubstrings(beta))
print(solution.countGoodSubstrings1(beta))