from collections import deque


def remove_vertices(graph):

    q = deque()
    for node, friends in graph.items():
        if len(friends) == 2:
            q.appendleft(node)

    while q:
        node = q.pop()
        if len(graph[node]) != 2:
            continue
        left, right = graph[node]

        if left in graph:
            graph[left].remove(node)

        if right in graph:
            graph[right].remove(node)

        del graph[node]

        if left in graph and right not in graph[left]:
            graph[left].append(right)

        if right in graph and left not in graph[right]:
            graph[right].append(left)

        if right in graph and len(graph[right]) == 2:
            q.appendleft(right)

        if left in graph and len(graph[left]) == 2:
            q.appendleft(left)

    return graph


graph = {
    "1": ["2", "4"],
    "2": ["1", "4", "3", "5"],
    "3": ["2", "4", "5", "6"],
    "4": ["1", "3", "2"],
    "5": ["2", "3", "6"],
    "6": ["3", "5"]
}
print(remove_vertices(graph))