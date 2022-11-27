from collections import deque, defaultdict


def count_shortest_paths(graph, start, end):
    q = deque([start])
    path_count = defaultdict(int)
    path_count[start] = 1

    while path_count[end] == 0:
        next_level_counts = defaultdict(int)
        for _ in range(len(q)):
            node = q.pop()

            for friend in graph[node]:
                if friend not in path_count:
                    path_count[friend] = 0
                    q.appendleft(friend)
                next_level_counts[friend] += path_count[node]

        for n, c in next_level_counts.items():
            path_count[n] += c

    return path_count[end]

graph = {
    "0": ["1", "2"],
    "1": ["3", "2"],
    "2": ["3"],
    "3": ["4", "5"],
    "4": ["6"],
    "5": ["6"],
    "6": []
}

print(count_shortest_paths(graph, "0", "6"))