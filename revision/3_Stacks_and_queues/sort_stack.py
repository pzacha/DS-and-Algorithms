import unittest


class SortStack:
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, data):
        self.stack.append(data)
        self.sort()

    def my_pop(self):
        self.is_empty()
        return self.stack2.pop()

    def sort(self):
        self.is_empty()
        data = self.stack.pop()
        if len(self.stack2) == 0:
            self.stack2.append(data)
        else:
            while len(self.stack2) != 0 and data < self.peek():
                self.stack.append(self.stack2.pop())
            self.stack2.append(data)
            while len(self.stack):
                self.stack2.append(self.stack.pop())

    def peek(self):
        self.is_empty()
        return self.stack2[-1]

    def is_empty(self):
        if len(self.stack) == 0 and len(self.stack2) == 0:
            raise Exception("Stack is empty")


class Test(unittest.TestCase):
    test_data = SortStack()
    test_data.push(10)
    test_data.push(7)
    test_data.push(9)
    test_data.push(3)

    def test_sort_stack(self):
        self.assertEqual(self.test_data.stack2, [3, 7, 9, 10])


if __name__ == "__main__":
    unittest.main()
