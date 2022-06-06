# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left_node = head
        right_node = head

        while right_node and right_node.next:
            right_node = right_node.next
            if right_node:
                right_node = right_node.next
            left_node = left_node.next

        return left_node


solution = Solution()
# 3
print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).val)

# 4
print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))).val)

