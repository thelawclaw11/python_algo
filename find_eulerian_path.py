from collections import defaultdict

# def all_nodes_have_even_degree(graph):
#     pass
#

def find_eulerian_path(graph):
    inn = defaultdict(int)
    out = defaultdict(int)

    for node, friends in graph.items():
        for friend in friends:
            inn[friend] += 1
            out[node] += 1

    start = None

    if all(inn[node] == out[node] for node in graph.keys()):
        start = list(graph.keys())[0]

    for node in graph:
        if out[node] == inn[node] + 1:
            if start is not None:
                return None
            start = node
    result = []
    seen_order = []

    def dfs(node):
        for friend in graph[node]:
            graph[node].remove(friend)
            seen_order.append((node, friend))
            dfs(friend)

        result.append(node)

    dfs(start)
    result.reverse()

    if len(result) - 1 == sum(out.values()):
        return result

    return None



graph = {
    "1": ["2", "3"],
    "2": ["2", "4", "4"],
    "3": ["5", "2", "1"],
    "4": ["6", "3"],
    "5": ["6"],
    "6": ["3"]
}

print(find_eulerian_path(graph))

# graph = {
#     "1": ["2", "5", "4", "3"],
#     "2": ["1", "5", "4", "3"],
#     "3": ["2", "1", "4", "5"],
#     "4": ["1", "2", "6", "3"],
#     "5": ["1", "2", "3", "6"],
#     "6": ["5", "4"]
# }