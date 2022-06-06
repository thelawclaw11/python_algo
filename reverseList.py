from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


def print_linked_list(head: ListNode):
    items = []

    current = head
    while current:
        items.append(current.val)
        current = current.next

    print(items)


solution = Solution()

print_linked_list(solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))