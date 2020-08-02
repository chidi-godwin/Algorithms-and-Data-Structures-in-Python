class Queue:
    def __int__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return queue[0]
        