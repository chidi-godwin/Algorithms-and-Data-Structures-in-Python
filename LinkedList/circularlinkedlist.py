from .doublylinkedlist import DoublyLinkedList, Node


class CircularLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.tail.next_node = self.head
            self.head.prev_node = self.tail
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            self.head.prev_node = self.tail

    def insert_end(self, data):
        """insert data at the end of linked list"""
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.tail.next_node = self.head
            self.head.prev_node = self.tail
            return

        new_node.prev_node = self.tail
        self.tail.next_node = new_node
        self.tail = new_node
        self.tail.next_node = self.head

    def traverse(self):
        """ print all elements in list"""

        actual_node = self.head

        while actual_node:
            if actual_node == self.tail:
                print(F"{actual_node.data}")
                break
            else:
                print(f"{actual_node.data}")
                actual_node = actual_node.next_node
            

    def reverse_traverse(self, actual_node=None):

        if not actual_node:
            actual_node = self.head

        if actual_node.next_node and actual_node.next_node != self.head:
            self.reverse_traverse(actual_node.next_node)

        print(f"{actual_node.data}")

    def remove(self, data):
        if self.head is None:
            return
        
        current_node = self.search(data)

        if not current_node:
            return f"{data} is not in list"
        elif current_node == self.head:
            self.size -= 1
            current_node.next_node.prev_node = current_node.prev_node
            current_node.prev_node.next_node = current_node.next_node
            self.head = current_node.next_node
        elif current_node == self.tail:
            self.size -= 1
            current_node.next_node.prev_node = current_node.prev_node
            current_node.prev_node.next_node = current_node.next_node
            self.tail = current_node.prev_node
        else:
            self.size -= 1
            current_node.next_node.prev_node = current_node.prev_node
            current_node.prev_node.next_node = current_node.next_node
            