class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def insert_start(self, data):
        """ insert data at the beginnig of the linked list """ 
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        """insert data at the end of linked list O(N)"""
        self.size += 1
        actual_node = self.head
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
            
        while actual_node.next_node:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse(self):
        """print all elements in list""" 

        actual_node = self.head

        while actual_node:
            print(f"{actual_node.data}")
            actual_node = actual_node.next_node

    def remove(self, data=None):
        """remove given data from list""" 

        if self.head is None:
            return

        self.size -= 1
        current_node = self.head
        previous_node = None

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        
        if not current_node:
            return f"{data} is not in list."
        elif previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node