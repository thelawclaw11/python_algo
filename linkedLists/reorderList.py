from collections import deque
from typing import Optional

from linkedLists.ListNode import ListNode
from linkedLists.array_to_linked_list import array_to_linked_list
from linkedLists.linked_list_to_array import linked_list_to_array


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        queue = deque()
        counter = 0
        current = head

        while current and counter <= (length // 2):
            queue.append(current)
            counter += 1
            current = current.next

        stack = deque()

        while current:
            stack.append(current)
            current = current.next

        dummy_head = ListNode()

        end = dummy_head

        while len(queue) > 0 or len(stack) > 0:
            front_of_queue = queue.popleft()
            end.next = front_of_queue
            end = end.next
            if len(stack) > 0:
                top_of_stack = stack.pop()
                end.next = top_of_stack
                end = end.next

        print(head)

        return head


solution = Solution()

head = array_to_linked_list([1,2,3,4,5])

solution.reorderList(head)

print(linked_list_to_array(head))