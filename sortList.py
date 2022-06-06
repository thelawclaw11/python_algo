from typing import Optional
from linkedLists.array_to_linked_list import array_to_linked_list
from linkedLists.linked_list_to_array import linked_list_to_array


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(left, right):
            dummy_head = ListNode()
            end = dummy_head

            l = left
            r = right

            while l != None and r != None:
                if l.val < r.val:
                    end.next = l
                    end = end.next
                    l = l.next
                else:
                    end.next = r
                    end = end.next
                    r = r.next

            while l != None:
                end.next = l
                end = end.next
                l = l.next

            while r != None:
                end.next = r
                end = end.next
                r = r.next
            return dummy_head.next

        def merge_sort(h):
            if h == None:
                return None

            if h.next == None:
                return h

            fast = h
            prev = None
            slow = h

            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            prev.next = None

            left = merge_sort(h)
            right = merge_sort(slow)

            return merge(left, right)

        return merge_sort(head)


solution = Solution()

input = array_to_linked_list([5,4,2,1,3])

result = solution.sortList(input)

print(linked_list_to_array(result))