def square_directed_graph(graph):
    square = {node: set() for node in graph}

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            neighbor2s = graph[neighbor]
            for neighbor2 in neighbor2s:
                square[node].add(neighbor2)

    return square




graph = {
    "a": {"c", "b"},
    "b": {"a", "e"},
    "c": {"d"},
    "d": set(),
    "e": {"d"}
}

expected = {
    "a": {"a", "d", "e"},
    "b": {"b", "d", "c"},
    "c": set(),
    "d": set(),
    "e": set()
}

assert(square_directed_graph(graph) == expected)
