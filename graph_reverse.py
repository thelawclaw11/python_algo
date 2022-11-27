def reverse_graph(graph):
    result = {k: [] for k in graph.keys()}

    for n, neighbors in graph.items():
        for neighbor in neighbors:
            result[neighbor].append(n)
    return result






