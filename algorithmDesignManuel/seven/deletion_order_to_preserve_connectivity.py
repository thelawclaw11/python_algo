def find_deletion_order(graph):

    result = []
    visited = set()

    def dfs(node):
        if node in visited:
            return

        visited.add(node)

        for friend in graph[node]:
            dfs(friend)

        result.append(node)

    dfs(list(graph.keys())[2])

    return result

graph = {
    "1": ["2", "3"],
    "2": ["1", "3"],
    "3": ["1", "2", "4"],
    "4": ["3", "5", "6"],
    "5": ["4", "6"],
    "6": ["4", "5"]
}

print(find_deletion_order(graph))