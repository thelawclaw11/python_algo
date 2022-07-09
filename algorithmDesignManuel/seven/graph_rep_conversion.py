import dataclasses


def matrix_to_list(matrix, nodes):
    graph = {n: [] for n in nodes}
    m = len(matrix)
    for row in range(m):
        for col in range(m):
            if matrix[row][col] == 1:
                graph[nodes[row]].append(nodes[col])

    return graph

def al_to_incidence_matrix(al, sorted_nodes):
    edges = set()

    for n, neighbors in al.items():
        for neighbor in neighbors:
            edge = [n, neighbor]
            edge.sort()
            edges.add(tuple(edge))

    edges = list(edges)

    edges.sort()

    incidence_matrix = [[0] * len(edges) for _ in range(len(sorted_nodes))]

    nodes_table = {n: i for i, n in enumerate(sorted_nodes)}

    for edge_index in range(len(edges)):
        s, e, = edges[edge_index]

        incidence_matrix[nodes_table[s]][edge_index] = 1
        incidence_matrix[nodes_table[e]][edge_index] = 1

    return incidence_matrix

def incidence_matrix_to_adj_list(im):
    rows = len(im)
    cols = len(im[0])
    result = [[] for _ in im]

    for col in range(cols):
        edge = []
        for row in range(rows):
            if im[row][col] == 1:
                edge.append(row)
                if len(edge) == 2:
                    break

        result[edge[0]].append(edge[1])
        result[edge[1]].append(edge[0])

    return result


im = [
    [1,1,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [0,0,1,0],
]

adj = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0]
]

print(incidence_matrix_to_adj_list(im))




