import dataclasses
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:



        while slow:
            if fast == slow and fast != head:
                first_meet = fast
                break

            fast = fast.next.next if fast.next else fast.next
            slow = slow.next

        if first_meet is None:
            return None

        a = head
        b = first_meet

        while True:
            if a == b:
                return a

            a = a.next
            b = b.next


s = Solution()

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = b

print(s.detectCycle(a))
