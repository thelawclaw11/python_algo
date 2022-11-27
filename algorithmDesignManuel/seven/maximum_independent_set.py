from dataclasses import dataclass, field


@dataclass
class Node:
    val: int
    weight: int
    children: list['Node']


def find_max_independent_set(root: Node):
    def f(node: Node, can_be_in_set):

        result_weight, result_set = 0, []

        if can_be_in_set:
            in_weight = node.weight
            in_set = [node.val]

            for child in node.children:
                w, s = f(child, False)
                in_weight += w
                in_set.extend(s)

            if in_weight > result_weight:
                result_weight = in_weight
                result_set = in_set

        without_weight = 0
        without_set = []

        for child in node.children:
            w, s = f(child, True)
            without_weight += w
            without_set.extend(s)

        if without_weight > result_weight:
            result_weight = without_weight
            result_set = without_set

        return result_weight, result_set

    return f(root, True)


t = Node(1, 1,
         [
             Node(2, 1, []),
             Node(3, 1, [
                 Node(5, 1, []), Node(6, 1, [])
             ]),
             Node(4, 1,
                  [
                      Node(7, 1, []),
                      Node(8, 1, []),
                      Node(9, 1, [])
                  ])
         ])

print(find_max_independent_set(t))