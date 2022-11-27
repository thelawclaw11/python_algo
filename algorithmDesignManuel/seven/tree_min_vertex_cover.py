from functools import cache


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



@cache
def find_min_size_vertex_cover(root, must_include_root):
    if not root:
        return [], 0

    if must_include_root:
        return [root.val] + find_min_size_vertex_cover(root.left, False) + find_min_size_vertex_cover(root.right, False)

    with_root = [root.val] + find_min_size_vertex_cover(root.left, False) + find_min_size_vertex_cover(root.right, False)
    without_root = find_min_size_vertex_cover(root.left, True) + find_min_size_vertex_cover(root.right, True)

    return with_root if len(with_root) < len(without_root) else without_root

alpha = Node(1, Node(2, Node(4), Node(5, Node(9))), Node(3, None, Node(7, None, Node(8))))


# print(find_min_weight_vertex_cover(alpha, False))

# print(find_min_size_vertex_cover(alpha, False))