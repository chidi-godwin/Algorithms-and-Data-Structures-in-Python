class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def pop(self):
        if not self.stack.is_empty():
            return self.stack.pop()
        return

    def peek(self):
        return self.stack[-1]

    def push(self, data):
        self.stack.append(data)

    @property
    def size(self):
        return len(self.stack)