def generate_all_subsets(nodes):
    result = []
    accum = []

    def F(i):
        if i >= len(nodes):
            result.append(accum[:])
            return

        F(i + 1)
        accum.append(nodes[i])
        F(i + 1)
        accum.pop()
    F(0)
    return result

# nodes = ["1", "2", "3", "4", "5", "6", "7"]
#
# print(generate_all_subsets((nodes)))


def verify_subset_is_cover(subset, graph):
    nodes_covered = {node for node in subset}

    for node in subset:
        for neighbor in graph[node]:
            nodes_covered.add(neighbor)

    return len(nodes_covered) == len(graph)


def find_all_minimum_covers(graph):
    nodes = list(graph.keys())
    subsets = generate_all_subsets(nodes)

    result = [nodes]

    for subset in subsets:
        is_cover = verify_subset_is_cover(subset, graph)

        if is_cover:
            if len(subset) < len(result[0]):
                result = [subset]
            elif len(subset) == len(result[0]):
                result.append(subset)
    return result


def find_minimum_vertex_cover_slow(graph):
    nodes = list(graph.keys())

    subsets = generate_all_subsets(nodes)
    result = []

    for subset in subsets:
        if verify_subset_is_cover(subset, graph) and (not result or len(subset) < len(result)):
            result = subset

    return result


def find_minimum_vertex_cover(raw_tree):
    tree = raw_tree.copy()
    result = set()

    while True:
        leaves = set()
        for node in tree:
            if len(tree[node]) == 1:
                leaves.add(node)

        if not leaves:
            break

        parents = set()

        for leaf in leaves:
            parent = tree[leaf].pop()
            tree[parent].discard(leaf)
            parents.add(parent)
            del tree[leaf]

        result |= parents

        grandparents = set()

        for parent in parents:
            if parent not in tree:
                continue
            grandparent = tree[parent].pop()
            if grandparent in tree:
                tree[grandparent].discard(parent)
            grandparents.add(grandparent)
            del tree[parent]

        great_grandparents = set()

        for grandparent in grandparents:
            if grandparent not in tree:
                continue

            great_grandparent = tree[grandparent].pop()
            if great_grandparent in tree:
                tree[great_grandparent].discard(grandparent)

            great_grandparents.add(great_grandparent)
            del tree[grandparent]

    return result

graph = {
    "0": {"1"},
    "1": {"0", "2", "3"},
    "2": {"1", "4", "5"},
    "3": {"1", "7"},
    "4": {"2", "6"},
    "5": {"2", "8", "9"},
    "6": {"4"},
    "7": {"3"},
    "8": {"5"},
    "9": {"5"},

}

# print(verify_subset_is_cover(["4", "5", "1", "3"], graph))

# expected = {"4", "5", "3"}
#
# print(find_all_minimum_covers(graph))

# cover_slow = find_minimum_vertex_cover_slow(graph)
# print(cover_slow)
# assert cover_slow == expected

cover = find_minimum_vertex_cover(graph)
# print(cover)
# assert cover == expected
