class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_start(self, data):
        """insert data at the start of the linked list"""
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        """insert data at the end of linked list"""
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head
            return

        new_node.prev_node = self.tail
        self.tail.next_node = new_node
        self.tail = new_node

    def traverse(self):
        """ print all elements in list"""

        actual_node = self.head

        while actual_node:
            print(f"{actual_node.data}")
            actual_node = actual_node.next_node

    def reverse_traverse(self, actual_node=None):

        if not actual_node:
            actual_node = self.head

        if actual_node.next_node:
            self.reverse_traverse(actual_node.next_node)

        print(f"{actual_node.data}")

    def search(self, data):

        if self.head is None:
            return

        current_node = self.head

        while current_node and current_node.data != data:
            current_node = current_node.next_node

        return current_node

    def remove(self, data):
        """remove given data from list"""

        if self.head is None:
            return

        self.size -= 1
        current_node = self.search(data)

        if not current_node:
            return f"{data} is not in list"
        else:
            current_node.next_node.prev_node = current_node.prev_node
            current_node.prev_node.next_node = current_node.next_node
