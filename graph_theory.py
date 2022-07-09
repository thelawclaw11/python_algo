import random


def find(array, func):
    for e in array:
        if func(e):
            return e
    return None


def cost_of_walk(graph, walk):
    result = 0

    for i in range(len(walk) - 1):
        cur = walk[i]
        nex = walk[i + 1]

        weight = find(graph[cur], lambda edge: edge[0] == nex)[1]
        if weight is None:
            raise Exception("Walk must be in graph")
        result += weight

    return result


def make_walk(graph, size):
    n = len(graph)

    start = random.randrange(0, n)

    walk = []
    current = start
    while len(walk) < size:
        nex = random.choice(graph[current])
        walk.append(nex)
        current = nex

    return walk


def make_trail(graph):
    pass


def verify_walk(graph, walk):

    for i in range(len(walk) - 1):
        cur = walk[i]
        nex = walk[i + 1]

        if cur not in graph[nex]:
            return False

    return True


def verify_tail(graph, trail):

    seen = set()

    for i in range(len(trail) - 1):
        cur = trail[i]
        nex = trail[i + 1]

        if cur not in graph[nex] or (cur, nex) in seen or (nex, cur) in seen:
            return False

        seen.add((cur, nex))

    return True

graph = [
    [1, 5],
    [0, 2, 4, 3],
    [1, 3],
    [1, 2, 5],
    [1, 5],
    [3, 4, 0]
]

walk =make_walk(graph, 100)

print(walk)
print(verify_walk(graph, walk))

