from .linkedlist import LinkedList


class LinkedListCreate(LinkedList):

    def __init__(self, iterable=(), *, sort=False, head=True, start='end'):
        super().__init__()
        self.iter = list(iterable)
        self.__create_linked_list(self.iter, sort, head, start)

    def to_list(self):
        return self.iter

    def __create_linked_list(self, iterable, sort, head, start):

        if sort:
            iterable.sort()

        if start == 'begin':
            iterable = iterable[::-1]

        if head:
            for _ in range(len(iterable)):
                self.insert_start(iterable.pop())
        else:
            for _ in range(len(iterable)):
                self.insert_end(iterable.pop())
