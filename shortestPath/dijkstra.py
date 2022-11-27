import math
from heapq import heappop, heappush


def dijkstra(graph, start, end):

    dist = {n: math.inf for n in graph.keys()}
    prev = {n: None for n in graph.keys()}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        node_dist, node = heappop(pq)
        visited.add(node)

        if node_dist > dist[node]:
            continue

        for friend, weight in graph[node]:
            if friend in visited:
                continue
            new_dist = dist[node] + weight
            if new_dist < dist[friend]:
                prev[friend] = node
                dist[friend] = new_dist
                heappush(pq,(new_dist, friend))

    cur = end
    path = []
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    path.reverse()

    return dist[end], path

def dijkstra2(graph, start):

    dist = {n: math.inf for n in graph.keys()}
    dist[start] = 0
    prev = {n: None for n in graph.keys()}

    q = [(0, start)]
    visited = set()

    while q:
        node_dist, node = heappop(q)

        visited.add(node)

        if node_dist > dist[node]:
            continue

        for friend, weight in graph[node]:
            if friend in visited:
                continue

            new_dist = weight + dist[node]
            if new_dist < dist[friend]:
                dist[friend] = new_dist
                heappush(q, (dist[friend], friend))

    return dist





a = {
    "0": [("1", 4), ("2", 1)],
    "1": [("3", 1)],
    "2": [("1", 2), ("3", 5)],
    "3": [("4", 3)],
    "4": []
}

print(dijkstra2(a, "0", ))