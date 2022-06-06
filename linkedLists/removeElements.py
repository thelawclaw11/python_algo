from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(nums):
    dummy_head = ListNode()
    end = dummy_head

    for n in nums:
        node = ListNode(n)
        end.next = node
        end = end.next
    return dummy_head.next


def linked_list_to_array(head):
    items = []

    current = head
    while current:
        items.append(current.val)
        current = current.next

    return items


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy_head = ListNode(None)
        dummy_head.next = head

        prev = dummy_head
        current = head
        while current:
            while current and current.val == val:
                current = current.next

            prev.next = current
            prev = current

            if current:
                current = current.next

        return dummy_head.next


solution = Solution()
print(linked_list_to_array(solution.removeElements(array_to_linked_list([7, 7, 7, 7]), 7)))