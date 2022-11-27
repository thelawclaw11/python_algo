def kcycle(graph, k):
    visited = set()

    def dfs(node, path_length):
        if node in visited:
            pass



    for node in graph:
        if node in visited:
            continue
        r = dfs(node, 0)
        if not r:
            return False

    return True





graph = {
}

print(kcycle(graph, 4))