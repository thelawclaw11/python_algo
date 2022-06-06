# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        items = []

        current = head
        while current:
            items.append(current.val)
            current = current.next

        if len(items) % 2 == 0:
            mid = len(items) // 2
            left_half = items[0:mid]
            right_half = items[mid:]
            left_half.reverse()

            return left_half == right_half
        else:
            mid = len(items) // 2
            left_half = items[0:mid]
            right_half = items[mid + 1:]

            left_half.reverse()
            return left_half == right_half

solution = Solution()

# print(solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(solution.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))))