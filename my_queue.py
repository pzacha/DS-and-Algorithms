class MyQueue:
    def __init__(self):
        self.my_queue = []
    
    def add(self, data):
        self.my_queue.append(data)

    def remove(self):
        if len(self.my_queue) > 0:
            output = self.my_queue[0]
            self.my_queue.pop(0)
            return output
        else:
            print("Queue is empty")

    def peek(self):
        if len(self.my_queue) > 0:
            print(self.my_queue[0])
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.my_queue) == 0

q = MyQueue()
q.add(1)
q.add(2)
q.peek()
q.remove()
q.peek()