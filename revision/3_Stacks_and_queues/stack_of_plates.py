import unittest


class Stack:
    def __init__(self, threshold):
        self.stack = [[]]
        self.threshold = threshold

    def push(self, data):
        if len(self.stack[-1]) == self.threshold:
            self.stack.append([data])
        else:
            self.stack[-1].append(data)

    def pop(self):
        if len(self.stack[-1]) > 0:
            output = self.stack[-1][-1]
            del self.stack[-1][-1]
            if len(self.stack[-1]) == 0:
                del self.stack[-1]
            return output
        else:
            raise Exception("Stack is empty")


class Test(unittest.TestCase):
    test_data = Stack(3)
    for i in range(10):
        test_data.push(i + 1)

    def test_stack_of_plates(self):
        self.assertEqual(self.test_data.stack, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])
        for i in range(2):
            output = self.test_data.pop()
        self.assertEqual(self.test_data.stack, [[1, 2, 3], [4, 5, 6], [7, 8]])
        self.assertEqual(output, 9)


if __name__ == "__main__":
    unittest.main()
