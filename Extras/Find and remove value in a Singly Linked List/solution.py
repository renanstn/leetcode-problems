class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("END")


def remove_value_from_singly_linked_list(linked_list, value_to_find: int):
    """
    FIXME: Do modo que está resolvido atualmente, irá quebrar caso o valor
    buscado seja o primeiro da lista.
    """
    current_node = linked_list.head
    previous_node = linked_list.head

    while current_node:
        if current_node.data == value_to_find:
            print("FIND")
            previous_node.next_node = current_node.next_node
        previous_node = current_node
        current_node = current_node.next_node


linked_list = SinglyLinkedList()
linked_list.append(23)
linked_list.append(11)
linked_list.append(7)
linked_list.append(48)
linked_list.append(119)
print("\nBefore")
linked_list.display()

remove_value_from_singly_linked_list(linked_list, 7)

print("\nAfter")
linked_list.display()
