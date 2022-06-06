import math
from collections import defaultdict
from typing import List

def print_table(table):
    for row in table:
        line = ''.join(str(row))
        print(line)

class Solution:
    def findLength(self, a: List[int], b: List[int]) -> int:
        N, M = len(a), len(b)

        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        output = 0

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                output = max(output, dp[i][j])
        return output




solution = Solution()


# 3
print(solution.findLength([2,3,2,1], [3,2,1,4]))

# print(solution.findLength([3, 2, 1], [3,2,1,4]))

# print(solution.findLength([0,0], [0,0]))

# print(solution.findLength([0, 1, 0, 0], [0, 0, 1, 0]))


# class Solution:
#     def findLength(self, a: List[int], b: List[int]) -> int:
#         memo = {}
#
#         def F(a_end, b_end, count):
#             key = f"{a_end},{b_end},{count}"
#             if key in memo:
#                 return memo[key]
#             if a_end == -1 or b_end == -1:
#                 return count
#
#             result = max(count,
#                        max(
#                            F(a_end - 1, b_end, 0),
#                            F(a_end, b_end - 1, 0),
#                            F(a_end - 1, b_end - 1, count + 1) if a[a_end] == b[b_end] else -math.inf
#                        )
#                        )
#
#             memo[key] = result
#             return result
#
#         return F(len(a) - 1, len(b) - 1, 0)
#
#
# solution = Solution()