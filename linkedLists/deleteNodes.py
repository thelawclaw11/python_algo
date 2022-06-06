from ListNode import ListNode
from array_to_linked_list import array_to_linked_list
from linked_list_to_array import linked_list_to_array

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:

        deleting = 0
        keeping = 0
        left = None

        is_keeping = True

        current = head
        while current:
            if is_keeping:
                keeping += 1

                if keeping == m:
                    is_keeping = False
                    deleting = 0
                    left = current
            else:
                deleting += 1

                if deleting == n:
                    is_keeping = True
                    keeping = 0
                    left.next = current.next
                    left = None

            current = current.next

        if left is not None:
            left.next = None

        return head

solution = Solution()

input = array_to_linked_list([1,2,3,4,5,6,7,8,9,10,11,12,13])

out = solution.deleteNodes(input, 2, 3)

print(linked_list_to_array(out))
