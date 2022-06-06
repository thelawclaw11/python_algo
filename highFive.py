import heapq
from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)

        for item in items:
            heapq.heappush(scores[item[0]], item[1])

        result = []

        for ID, heap in scores.items():
            top_five_average = sum(heapq.nlargest(5, heap)) // 5
            result.append([ID, top_five_average])

        result.sort(key=lambda x: x[0], reverse=True)

        return result

solution = Solution()
solution.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
