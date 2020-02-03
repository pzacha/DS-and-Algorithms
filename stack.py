class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            output = self.stack[-1]
            self.stack.pop()
            return output
        else:
            print("Stack is empty")

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(1)
s.push(4)
s.peek()
s.pop()
s.peek()
