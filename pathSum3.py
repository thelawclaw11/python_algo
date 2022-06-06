# Definition for a binary tree node.
from get_binary_tree_paths import binary_tree_from_array


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        result = 0

        def F(node, current_sum):
            nonlocal result
            if current_sum + node.val == targetSum:
                result += 1

            if node.left:
                F(node.left, current_sum + node.val)

            if node.right:
                F(node.right, current_sum + node.val)

        def G(node):
            if not node:
                return

            F(node, 0)

            if node.left:
                G(node.left)

            if node.right:
                G(node.right)
        G(root)

        return result


solution = Solution()


# target = 8, answer = 3
gamma = binary_tree_from_array([10,5,-3,3,2,None,11,3,-2,None,1])
# target = 3, answer = 2
delta = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))

print(solution.pathSum(delta, 3))
print(solution.pathSum(gamma, 8))