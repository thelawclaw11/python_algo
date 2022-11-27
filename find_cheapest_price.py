import math
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {n: list() for n in range(n)}

        for start, end, cost in flights:
            graph[start].append((end, cost))

        table = {n: defaultdict(lambda: math.inf) for n in range(n)}
        table[src][0] = 0

        max_flight_count = k + 1

        pq = [(0, 0, src)]
        visited = set()

        while pq:
            dist, flight_count, node = heappop(pq)

            if dist > table[node][flight_count]:
                continue

            visited.add((node, flight_count))

            for neighbor, dist_to_neighbor in graph[node]:
                if (neighbor, flight_count + 1) in visited:
                    continue

                new_dist = table[node][flight_count] + dist_to_neighbor
                if new_dist < table[neighbor][flight_count + 1]:
                    table[neighbor][flight_count + 1] = new_dist
                    heappush(pq, (new_dist, flight_count, neighbor))

        print(table)