import math
from random import randint

class MinFinder:
    def __init__(self, array):
        self.table = {}
        for start in range(len(array)):
            minn = array[start]
            for end in range(start, len(array)):
                minn = min(array[end], minn)
                self.table[(start, end)] = minn

    def find_min(self, start, end):

        return self.table[(start, end)]

class Node:
    def __init__(self):
        self.start = None
        self.end = None
        self.val = None
        self.left = None
        self.right = None

class MinFinder2:
    def __init__(self, array):
        def F(start, end):
            node = Node()
            node.start = start
            node.end = end

            if start == end:
                node.val = array[start]
                return node

            mid = (start + end) // 2

            left = F(start, mid)
            right = F(mid + 1, end)

            node.left = left
            node.right = right
            node.val = min(left.val, right.val)
            return node

        self.root = F(0, len(array) - 1)

    def find_min(self, start, end):

        def F(node):
            if not node or node.end < start or node.start > end:
                return math.inf

            if node.start >= start and node.end <= end:
                return node.val

            left_result = F(node.left)
            right_result = F(node.right)
            
            return min(left_result, right_result)

        return F(self.root)



alpha = [10, 2, 9, 3, 1, 0, 8, 5, 0, 6]
      # [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
min_finder = MinFinder2(alpha)


print(min_finder.find_min(6, 7))

# # 1
# print(min_finder.find_min(3, 4))
# #
# # 0
# print(min_finder.find_min(3, 7))
# #
# # #6
# print(min_finder.find_min(9, 9))

# print([randint(0, 10) for _ in range(10)])