def check(graph, e):
    start, end = e
    graph[start].remove(end)
    graph[end].remove(start)

    visited = set()

    def f(node):
        if node in visited:
            return

        visited.add(node)

        for friend in graph[node]:
            f(friend)

    f(end)

    return start in visited

graph = {
    "1": ["2"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["3"]
}

print(check(graph, ("2", "3")))