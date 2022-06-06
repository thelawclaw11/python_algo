from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, left: List[int], right: List[int], k: int) -> List[List[int]]:
        k = min(k, len(left) * len(right))

        heap = []
        uniq = set()

        l_start = 0
        l_end = 0

        r_start = 0
        r_end = 0

        result = []

        while len(result) < k:
            if l_end == len(left) and r_end == len(right):
                l_start += 1
                r_start += 1
                l_end = l_start
                r_end = r_start

            alpha = (left[l_start] + right[r_end], (left[l_start], right[r_end]), (l_start, r_end)) if l_start < len(left) and r_end < len(right) else None
            beta = (left[l_end] + right[r_start], (left[l_end], right[r_start]), (l_end, r_start)) if l_end < len(left) and r_start < len(right) else None

            if alpha is not None and alpha not in uniq:
                heappush(heap, alpha)
                uniq.add(alpha)

            if beta is not None and beta not in uniq:
                heappush(heap, beta)
                uniq.add(beta)

            best = heappop(heap)

            result.append(best[1])

            if l_end != len(left):
                l_end += 1

            if r_end != len(right):
                r_end += 1

        return result

def simple(left, right, k):
    pairs = []

    for i in range(len(left)):
        for j in range(len(right)):
            pairs.append( (left[i], right[j]))

    pairs.sort(key=lambda p: p[0] + p[1])

    return pairs[:k]



solution = Solution()
print(solution.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 10))

print(simple([1, 2, 4, 5, 6], [3, 5, 7, 9], 10))
