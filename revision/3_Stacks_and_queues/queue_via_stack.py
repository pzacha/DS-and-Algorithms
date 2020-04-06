import unittest


class StackQueue:
    def __init__(self):
        self.top = []
        self.bottom = []

    def add(self, data):
        self.bottom.append(data)

    def remove(self):
        self.is_empty()
        self.move_items()
        output = self.top.pop()
        return output

    def move_items(self):
        if len(self.top) == 0:
            for i in range(len(self.bottom)):
                self.top.append(self.bottom.pop())

    def is_empty(self):
        if len(self.top) == 0 and len(self.bottom) == 0:
            raise Exception("Stack is empty")


class Test(unittest.TestCase):
    test_data = StackQueue()
    for i in range(5):
        test_data.add(i + 1)
    for i in range(2):
        test_data.remove()
    for i in range(2):
        test_data.add(6 + i)

    def test_queue_via_stack(self):
        self.assertEqual(self.test_data.bottom, [6, 7])
        self.assertEqual(self.test_data.top, [5, 4, 3])


if __name__ == "__main__":
    unittest.main()
