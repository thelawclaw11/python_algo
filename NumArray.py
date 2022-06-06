from typing import List


class TreeNode:
    def __init__(self, val=None, start=None, end=None, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class NumArray:

    def __init__(self, nums: List[int]):

        def build_tree(left, right):
            if left == right:
                return TreeNode(nums[left], left, right)

            mid = (left + right) // 2
            left_node = build_tree(left, mid)
            right_node = build_tree(mid + 1, right)

            return TreeNode(left_node.val + right_node.val, left, right, left_node, right_node)

        self.root = build_tree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        def helper(node):
            nonlocal val

            if node.start == index and node.end == index:
                diff = val - node.val
                node.val = val
                return diff

            mid = (node.start + node.end) // 2
            diff = helper(node.right) if index > mid else helper(node.left)
            node.val += diff
            return diff

        helper(self.root)

    def sumRange(self, start: int, end: int) -> int:

        def helper(node):
            if node.start >= start and node.end <= end:
                return node.val

            if node.start > end or node.end < start:
                return 0

            return helper(node.left) + helper(node.right)

        return helper(self.root)







na = NumArray([1,2,3,4,5,6,7,8,9,10])

assert(na.sumRange(0,9) == 55)
assert(na.sumRange(0,5) == 21)
assert(na.sumRange(5,7) == 21)
assert(na.sumRange(9,9) == 10)

na.update(5, 20)

assert(na.sumRange(5,5) == 20)
assert(na.sumRange(5,6) == 27)
assert(na.sumRange(5,7) == 35)
assert(na.sumRange(5,9) == 14 + 40)
assert(na.sumRange(0,9) == 55 + 14)