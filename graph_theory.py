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


def is_eulerian(graph):

    for node, friends in graph:
        if len(friends) % 2 != 0:
            return False

    return True




graph = {
    "1": ["2", "5", "4", "3"],
    "2": ["1", "5", "4", "3"],
    "3": ["2", "1", "4", "5"],
    "4": ["1", "2", "6", "3"],
    "5": ["1", "2", "3", "6"],
    "6": ["5", "4"]
}


print(is_eulerian(graph))

