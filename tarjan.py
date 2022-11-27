import math
from collections import defaultdict


def tarjan(graph):
    stack = []
    low = {k: math.inf for k in graph.keys()}
    ids = {k: None for k in graph.keys()}
    visited = set()
    i = 0

    def dfs(node):
        nonlocal i
        ids[node] = i
        low[node] = i
        i += 1
        stack.append(node)
        visited.add(node)

        for friend in graph[node]:
            if ids[friend] is None:
                dfs(friend)

            if friend in visited:
                low[node] = min(low[node], low[friend])

        if low[node] == ids[node]:
            while True:
                n = stack.pop()
                visited.discard(n)
                if n == node:
                    break

    for l in graph.keys():
        if ids[l] is None:
            dfs(l)

    return low

g = {
    0: [1],
    1: [2],
    2: [0],
    3: [7, 4],
    4: [5],
    5: [0, 6],
    6: [0, 2, 4],
    7: [3, 5]
}

print(tarjan(g))