from linkedLists.ListNode import ListNode

def array_to_linked_list(nums):
    dummy_head = ListNode()
    end = dummy_head

    for n in nums:
        node = ListNode(n)
        end.next = node
        end = end.next
    return dummy_head.next
