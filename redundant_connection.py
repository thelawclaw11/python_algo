from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        print(graph)

        result = []
        visited = set()

        def search(node, prev):
            if node in visited:
                result.append([prev, node])
                return

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != prev:
                    search(neighbor, node)

            return None

        search(1, None)

        print(result)


solution = Solution()

print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))