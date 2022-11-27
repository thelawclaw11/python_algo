from functools import cache


class Node:
    def __init__(self, val, weight=0, children=None):
        if children is None:
            children = []
        self.val = val
        self.weight = weight
        self.children = children



def find_min_weight_vertex_cover(root: Node):


    @cache
    def f(node: Node, must_include_root: bool):
        if not node:
            return 0, []

        node_weight = node.weight

        with_node_weight = node_weight
        with_node_cover = [node.val]

        for child in node.children:
            weight, cover = f(child, False)
            with_node_weight += weight
            with_node_cover.extend(cover)

        if must_include_root:
            return with_node_weight, with_node_cover

        without_node_weight = 0
        without_node_cover = []

        for child in node.children:
            weight, cover = f(child, True)
            without_node_weight += weight
            without_node_cover.extend(cover)

        if with_node_weight < without_node_weight:
            return with_node_weight, with_node_cover

        return without_node_weight, without_node_cover

    return f(root, False)


tree = Node(1, -100,[
    Node(2, 5),
    Node(3,6,
         [
             Node(5, 1000)
         ]
         ),
    Node(4, 7)
])

print(find_min_weight_vertex_cover(tree))