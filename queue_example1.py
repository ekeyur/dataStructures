
class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items += [item]
        self.size += 1

    def dequeue(self):
        item = self.items[0]
        del self.items[0]
        self.size -= 1
        return item

    def size(self):
        return len(self.items)


q = Queue()
print q.isEmpty()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
print(q.items)
