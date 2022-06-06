def linked_list_to_array(head):
    items = []

    current = head
    while current:
        items.append(current.val)
        current = current.next

    return items