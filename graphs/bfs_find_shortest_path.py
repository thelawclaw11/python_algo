from collections import deque

def get_parent_table(graph, start):
    parent = {start: None}
    visited = {start}
    q = deque([start])

    while q:
        node = q.pop()

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                visited.add(neighbor)
                q.appendleft(neighbor)
    return parent

def get_shortest_path(graph, start, end):
    parent_table = get_parent_table(graph, start)

    path = [end]
    parent = parent_table[end]

    while parent != None:
        path.append(parent)
        parent = parent_table[parent]

    path.reverse()

    return path

def get_components(graph: dict):
    result = []
    visited = set()

    def bfs(root):
        nonlocal visited
        nodes = []

        q = deque([root])

        while q:
            node = q.pop()
            nodes.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.appendleft(neighbor)

        return nodes

    for node in graph.keys():
        if node not in visited:
            visited.add(node)
            result.append(bfs(node))

    return result

def has_cycle(graph):

    visited = set()

    def dfs(node, prev):
        nonlocal visited
        if node in visited:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != prev:
                result = dfs(neighbor, node)
                if result == True:
                    return True

        return False


    for node in graph.keys():
        if node not in visited:
            result = dfs(node, None)
            if result is True:
                return True

    return False

graph = {
    "1": ["2", "3", "4"],
    "2": ["1", "6"],
    "3": ["1", "5", "7"],
    "4": ["1", "7"],
    "5": ["3", "6"],
    "6": ["2", "5"],
    "7": ["3", "4"],
    "9": ["10", "11"],
    "10": ["9"],
    "11": ["9"],
    "12": []
}

# print(get_components(graph))

print(has_cycle(graph))

print(has_cycle({
    "1": ["2", "3"],
    "2": ["1"],
    "3": ["1"]
}))