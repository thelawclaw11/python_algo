# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from get_binary_tree_paths import TreeNode

# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#
#         def F(node, accum):
#             print(accum)
#             if node.left is None and node.right is None:
#                 return accum + [node.val]
#
#             both = []
#
#             if node.left:
#                 both.append(F(node.left, accum[copy] + node.val))
#
#             if node.right:
#                 both.append(F(node.right, accum[copy] + node.val))
#
#             return both
#
#         return F(root, [])

path = [1,0,1]

s = 0

for n in path:
    s = (s << 1 | n)

print(s)