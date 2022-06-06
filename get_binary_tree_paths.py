import pprint
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_from_array(array):
    root = TreeNode()

    def build(node, index):
        if node is None:
            return
        node.val = array[index]

        left_index = (index * 2) + 1
        right_index = (index + 1) * 2

        if right_index < len(array) and array[right_index] is not None:
            right_node = TreeNode()
            node.right = right_node
            build(right_node, right_index)
        if left_index < len(array) and array[left_index] is not None:
            left_node = TreeNode()
            node.left = left_node
            build(left_node, left_index)

    build(root, 0)

    return root

def get_binary_tree_paths(root):

    paths = []


    def F(node):
        nonlocal paths
        if node is None:
            return []

        both_sides = F(node.left) + F(node.right)

        both_sides_with_current = []

        for path in both_sides:
            both_sides_with_current.append([node.val] + path)

        both_sides_with_current.append([node.val])

        for path in both_sides_with_current:
            paths.append(path.copy())

        return both_sides_with_current

    F(root)

    print(len(paths))

    return paths


gamma = binary_tree_from_array([10,5,-3,3,2,None,11,3,-2,None,1])

# def count_paths(root):
#
#     def F(node):
#         if node is None:
#             return 0
#
#         result = 2 * (F(node.left) + F(node.right)) + 1
#
#         if node.left:
#             if node.left.left:
#                 result -= F(node.left.left)
#             if node.left.right:
#                 result -= F(node.left.right)
#
#         if node.right:
#             if node.right.left:
#                 result -= F(node.right.left)
#             if node.right.right:
#                 result -= F(node.right.right)
#
#         return result
#     return F(root)


# expected_result = TreeNode(10,
#                            TreeNode(5,
#                                     TreeNode(3,
#                                              TreeNode(3),
#                                              TreeNode(-1)),
#                                     TreeNode(2,
#                                              None,
#                                              TreeNode(1))),
#                            TreeNode(-3,
#                                     None,
#                                     TreeNode(11))
#                            )




