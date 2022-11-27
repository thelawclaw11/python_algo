def verify_complement(graph, complement):
    if set(graph.keys()) != set(complement.keys()):
        return False

    nodes = set(graph.keys())

    for node, neighbors in graph.items():
        condition = nodes - neighbors - {node} == complement[node]
        if not condition:
            return False

    return True



def get_complement(graph):
    complement = {n: set() for n in graph.keys()}
    nodes = set(graph.keys())

    for node, neighbors in graph.items():
        non_neighbors = nodes - neighbors - {node}
        complement[node] |= non_neighbors

    return complement

a = {
    "A": {"B", "D"},
    "B": {"E", "C", "A"},
    "C": {"D", "B"},
    "D": {"A", "C"},
    "E": {"B"}
}
comp = {'A': {'C', 'E'}, 'B': {'D'}, 'C': {'A', 'E'}, 'D': {'B', 'E'}, 'E': {'D', 'C', 'A'}}

print(get_complement(a))
print(verify_complement(a, comp))

