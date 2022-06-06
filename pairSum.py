# Definition for singly-linked list.
import mathHelp
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        items = []

        current = head

        while current:
            items.append(current.val)
            current = current.next

        best_sum = -math.inf
        i = 0
        j = len(items) - 1


        while i < j:
            current_sum = items[i] + items[j]
            print(current_sum)
            best_sum = max(best_sum, current_sum)
            i += 1
            j -= 1

        return best_sum



solution = Solution()
print(solution.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))))