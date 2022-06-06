from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L = list1
        R = list2

        dummy_head = ListNode()

        merged = dummy_head

        while R is not None and L is not None:
            if R is None:
                merged.next = L
                merged = merged.next
                L = L.next
            elif L is None:
                merged.next = R
                merged = merged.next
                R = R.next
            elif L.val == R.val:
                merged.next = R
                merged = merged.next
                merged.next = L
                merged = merged.next
                L = L.next
                R = R.next
            elif R.val < L.val:
                merged.next = R
                merged = merged.next
                R = R.next
            elif L.val < R.val:
                merged.next = L
                merged = merged.next
                L = L.next
        return dummy_head.next


solution = Solution()

solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))