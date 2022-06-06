# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trailing_node = head
        left_node = head
        right_node = head

        while right_node and right_node.next:
            right_node = right_node.next
            if right_node:
                right_node = right_node.next
            trailing_node = left_node
            left_node = left_node.next

        if trailing_node == head and left_node == head and right_node == head:
            # linked list has length 1
            return None

        if trailing_node == head and left_node == right_node:
            # linked list has length 2
            trailing_node.next = None
            return head

        trailing_node.next = left_node.next

        return head


def print_linked_list(head: ListNode):
    items = []

    current = head
    while current:
        items.append(current.val)
        current = current.next

    print(items)

solution = Solution()

# []
print_linked_list(solution.deleteMiddle(ListNode(1)))

# [2]
print_linked_list(solution.deleteMiddle(ListNode(2, ListNode(1))))

# [1,3]
print_linked_list(solution.deleteMiddle(ListNode(1, ListNode(2, ListNode(3)))))

# [1,2,4,5]
# print_linked_list(solution.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

# [1,2,3,5,6]
# print_linked_list(solution.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))