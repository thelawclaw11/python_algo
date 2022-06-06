from typing import List

class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_tree_values_in_order(root: Treenode):
    values: List[int] = []

    def traverse(node: Treenode):
        if node.left:
            traverse(node.left)
        values.append(node.val)
        if node.right:
            traverse(node.right)

    traverse(root)

    return values


class Solution:
    def increasingBST(self, root: Treenode):

        values = get_tree_values_in_order(root)
        dummy_root = Treenode()
        current = dummy_root

        for value in values:
            new_node = Treenode(value)
            current.right = new_node
            current = new_node

        return dummy_root.right

solution = Solution()

input = Treenode(5,
                Treenode(3,
                         Treenode(2,
                                  Treenode(1)),
                         Treenode(4)),
                Treenode(6,
                         None,
                         Treenode(8,
                                  Treenode(7),
                                  Treenode(9))))
print(get_tree_values_in_order(input))
print(get_tree_values_in_order(solution.increasingBST(input)))