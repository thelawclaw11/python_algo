from copy import copy, deepcopy


def is_connected(graph):
    item = deepcopy(graph.popitem())
    graph[item[0]] = item[1]

    seen = set()

    def visit(node):
        if node in seen:
            return
        seen.add(node)

        for friend in graph[node]:
            visit(friend)

    visit(item[0])

    return len(seen) == len(graph)


a = {
    "A": {"B", "D"},
    "B": {"E", "C", "A"},
    "C": {"D", "B"},
    "D": {"A", "C"},
    "E": {"B"}
}

b = {
    "A": {"B"},
    "B": {"E", "A"},
    "C": {"D"},
    "D": {"C"},
    "E": {"B"}
}

print(is_connected(b))
print(is_connected(a))
