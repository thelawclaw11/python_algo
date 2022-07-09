from collections import defaultdict


# def contains_triangle(graph):
#
#     depths = defaultdict(int)
#
#     def search(node, curr_depth):
#         if node in depths:
#             if abs(depths[node] - curr_depth) == 3:
#                 return True
#
#             return False
#
#         depths[node] = curr_depth
#
#         for neighbor in graph[node]:
#             res = search(neighbor, curr_depth + 1)
#             if res:
#                 return True
#
#         return False
#
#     for node in range(len(graph)):
#         if node not in depths:
#             if search(node, 0):
#                 return True
#
#     return False

def contains_triangle(graph):

    def search(start):
        visited = set()

        def F(node, depth):
            if node in visited and node == start and depth == 3:
                return node

            if node in visited or depth > 3:
                return None

            visited.add(node)

            for neighbor in graph[node]:
                res = F(neighbor, depth + 1)
                if res:
                    return res

            return None

        return F(start, 0)


    for node in range(len(graph)):
        res = search(node)
        if res:
            return res

    return None
















