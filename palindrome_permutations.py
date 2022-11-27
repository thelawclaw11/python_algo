from collections import Counter, deque
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        def is_palindrome(st):

            l = 0
            r = len(st) - 1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1

            return True

        result = []

        table = Counter(s)

        cur = deque()

        def get_palindromes():
            if len(cur) == len(s):
                result.append("".join(list(cur)))
                return

            for char, count in table.items():
                if count == 0:
                    continue

                if count % 2 == 1:
                    if len(cur) == 0:
                        table[char] -= 1
                        cur.append(char)
                        get_palindromes()
                        table[char] += 1
                        cur.pop()
                    else:
                        return
                else:
                    table[char] -= 2
                    cur.appendleft(char)
                    cur.append(char)
                    get_palindromes()
                    cur.pop()
                    cur.popleft()
                    table[char] += 2

        get_palindromes()

        return result

s = Solution()

print([1,2,3,4,5][1:-1])