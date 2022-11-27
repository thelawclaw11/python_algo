import math


def top_sort(graph):
    unmarked = set(graph.keys())
    temp = set()
    perm = set()

    result = []

    def visit(node):
        if node in perm:
            return

        if node in temp:
            raise ValueError()

        unmarked.discard(node)
        temp.add(node)

        for friend, weight in graph[node]:
            visit(friend)

        temp.discard(node)
        perm.add(node)
        result.append(node)

    while unmarked:
        visit(unmarked.pop())

    result.reverse()
    return result


def find_shortest_path(start, end, graph):
    top_order = top_sort(graph)

    cost = {n: math.inf for n in graph.keys()}
    prev = {n: None for n in graph.keys()}
    cost[start] = 0

    for node in top_order:
        for friend, weight in graph[node]:
            new_cost = cost[node] + weight
            if new_cost < cost[friend]:
                prev[friend] = node
                cost[friend] = new_cost

    path = []
    cur = end

    while True:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]
    path.reverse()

    return path, cost[end]


dag = {
    "A": [("B", 3), ("C", 6)],
    "B": [("E", 11), ("D", 4), ("C", 4)],
    "C": [("D", 8), ("G", 11)],
    "D": [("E", -4), ("F", 5), ("G", 2)],
    "E": [("H", 9)],
    "F": [("H", 1)],
    "G": [("H", 2)],
    "H": []
}

print(find_shortest_path("A", "H", dag))
