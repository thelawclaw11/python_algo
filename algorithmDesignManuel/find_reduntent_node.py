def find(graph):

    visited = set()

    def search(node, prev):
        if node in visited:
            return (prev, node)

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != prev:
                res = search(neighbor, node)
                if res:
                    return res

        return None

    return search(0, None)

graph = {
    0: [1, 2],
    1: [0, 3, 2],
    2: [1, 0],
    3: [1]
}


print(find(graph))