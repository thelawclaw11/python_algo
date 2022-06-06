from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def F(node, current_length):
            if not node:
                return current_length

            left_result = 0
            right_result = 0

            if node.left:
                if node.left.val == node.val:
                    left_result = F(node.left, current_length + 1)
                else:
                    left_result = F(node.left, 0)

            if node.right:
                if node.right.val == node.val:
                    right_result = F(node.right, current_length + 1)
                else:
                    right_result = F(node.left, 0)
                    

            return max(left_result, right_result)

        return F(root, 0)

solution = Solution()