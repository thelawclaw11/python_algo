from linkedLists.linked_list_to_array import linked_list_to_array


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        current_index = 0
        current = self.head
        while current and current_index <= index:
            if current_index == index:
                return current.val
            current_index += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.length:
            new_node = ListNode(val)

            left = self.head
            right = self.head.next
            right_index = 1

            while right_index != index:
                left = left.next
                right = right.next
                right_index += 1

            left.next = new_node
            new_node.next = right
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        elif index < self.length:

            left = self.head
            right = self.head.next
            right_index = 1
            while right_index != index:
                left = left.next
                right = right.next
                right_index += 1

            left.next = right.next

        self.length -= 1

        return None

my_list = MyLinkedList()
my_list.addAtHead(86)
my_list.addAtIndex(1, 54)
my_list.addAtIndex(1, 14)

my_list.addAtHead(83)

print(linked_list_to_array(my_list.head))

my_list.deleteAtIndex(4)

print(linked_list_to_array(my_list.head))

my_list.addAtIndex(3,18)

my_list.addAtHead(46)

print(my_list.get(5))
print(linked_list_to_array(my_list.head))



