from enum import Enum, auto


def top_sort(graph):
    parent_count = {node: 0 for node in graph.keys()}

    for node in graph:
        for neighbor in graph[node]:
            parent_count[neighbor] += 1

    visited = set()

    result = []

    def F(node):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            parent_count[neighbor] -= 1
            if parent_count[neighbor] == 0:
                F(neighbor)

    for node in graph:
        if parent_count[node] == 0:
            F(node)

    return result


def top_sort2(graph):
    result = []
    perm = set()
    temp = set()
    unmarked = set(graph.keys())

    def visit(node):
        nonlocal perm, temp, unmarked, result
        if node in perm:
            return
        if node in temp:
            raise Exception("This graph has a cycle")

        unmarked.discard(node)
        temp.add(node)

        for neighbor in graph[node]:
            visit(neighbor)

        temp.discard(node)
        perm.add(node)
        result.append(node)

    while unmarked:
        visit(unmarked.pop())

    result.reverse()

    return result


def top_sort3(graph):
    parent_count = {node: 0 for node in graph.keys()}

    for node, children in graph.items():
        for child in children:
            parent_count[child] += 1

    seen = set()
    result = []

    def visit(node):
        if node in seen:
            return

        seen.add(node)
        result.append(node)

        for c in graph[node]:
            parent_count[c] -= 1
            if parent_count[c] == 0:
                visit(c)

    for node in graph.keys():
        if parent_count[node] == 0:
            visit(node)

    if len(result) != len(graph):
        raise ValueError("Graph has a cycle")

    return result


class State(Enum):
    TEMP = auto()
    PERM = auto()
    UNMARKED = auto()

def top_sort4(graph):

    state = {n: State.UNMARKED for n in graph.keys()}

    result = []

    def visit(node):
        if state[node] == State.PERM:
            return

        if state[node] == State.TEMP:
            raise ValueError("Not a DAG")

        state[node] = State.TEMP

        for friend in graph[node]:
            visit(friend)

        state[node] = State.PERM
        result.append(node)


    while len([s for s in state.values() if s == State.UNMARKED]):
        visit([n for n, s in state.items() if s == State.UNMARKED][0])

    result.reverse()

    return result


dag2 = {
    "A": ["B", "D"],
    "B": ["C", "D", "E"],
    "C": ["F"],
    "D": ["E", "G"],
    "E": ["G", "F"],
    "F": [],
    "G": ["I"],
    "H": ["G", "J", "F"],
    "I": ["J"],
    "J": []
}

# print(top_sort(dag2))
# print(top_sort2(dag2))
# print(top_sort3(dag2))
print(top_sort4(dag2))

dag = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D", "F"],
    "D": [],
    "E": ["D"],
    "F": ["E"],
    "H": ["A", "B"],
    "G": ["A", "F"],
}

# print(top_sort(dag))
# print(top_sort2(dag))
