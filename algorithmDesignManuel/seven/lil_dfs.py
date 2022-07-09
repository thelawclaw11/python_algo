def dfs(graph):
    parent = {}
    entry = {}
    _exit = {}
    discovered = set()
    processed = set()
    time = 0

    def F(node):
        nonlocal time
        discovered.add(node)
        time += 1
        entry[node] = time

        for neighbor in graph[node]:
            if neighbor not in discovered and neighbor not in processed:
                parent[neighbor] = node
                F(neighbor)

        discovered.discard(node)
        processed.add(node)
        _exit[node] = time
        time += 1
    