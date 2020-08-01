class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            self.head = prev
            return
        next = node.get_next()
        node.set_next(prev)
        self.reverse_list(next, node)

    def printLinkedList(self):
        current_list = []
        node = self.head
        while node != None:
            current_list.append(node.value)
            node = node.get_next()
        return current_list


list = LinkedList()
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(5)
list.add_to_head(9)
list.add_to_head(12)


print(f"Head value is {list.head.value}")
print(f"Current list: {list.printLinkedList()}")
print("Reverse!")
list.reverse_list(list.head, None)
print(f"Current list: {list.printLinkedList()}")
print(f"Head value is {list.head.value}")
