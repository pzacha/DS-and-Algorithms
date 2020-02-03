class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self, data):
        self.queue.append(data)

    def remove(self):
        if len(self.queue) > 0:
            output = self.queue[0]
            self.queue.pop(0)
            return output
        else:
            print("Queue is empty")

    def peek(self):
        if len(self.queue) > 0:
            print(self.queue[0])
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.stack) == 0

q = Queue()
q.add(1)
q.add(2)
q.peek()
q.remove()
q.peek()