import unittest
import sys
import os

from LinkedList import LinkedList, DoublyLinkedList, LinkedListCreate

l = LinkedList()

class LinkedListTests(unittest.TestCase):

    global l
    def test_LinkedList(self):
        self.assertIsInstance(l, LinkedList)

    def test_insert_start(self):
        l.insert_start(7)
        self.assertIsNotNone(l.head)
        self.assertEqual(l.head.data, 7)

    def test_insert_end(self):
        l.insert_end(8)
        self.assertEqual(l.head.data, 8)

class DoublyLinkedListTests(unittest.TestCase):
    def test_DoublyLinkedList(self):
        l = DoublyLinkedList()
        self.assertIsInstance(l, DoublyLinkedList)


if __name__ == "__main__":
    unittest.main()
