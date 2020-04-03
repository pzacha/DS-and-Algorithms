import unittest


class MultiStack:
    def __init__(self, size):
        self.size = size
        self.stack = 3 * self.size * [0]
        self.sizes = size * [0]

    def push(self, data, stacknum):
        if stacknum not in [0, 1, 2]:
            raise Exception("Wrong stack number")
        if self.isFull(stacknum):
            raise Exception("Stack is full")
        self.stack[stacknum * self.size + self.sizes[stacknum]] = data
        self.sizes[stacknum] += 1

    def pop(self, stacknum):
        if self.sizes[stacknum] == 0:
            raise Exception("Stack is empty")
        output = self.stack[stacknum * self.size + self.sizes[stacknum]]
        self.stack[stacknum * self.size + self.sizes[stacknum]] = 0
        self.sizes[stacknum] -= 1
        return output

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.size:
            return True


class Test(unittest.TestCase):
    test_data = MultiStack(3)
    for i in range(3):
        test_data.push(i + 1, 0)
        test_data.push(i + 7, 1)
    test_data.push(9, 2)

    def test_three_in_one(self):
        self.assertEqual(self.test_data.stack, [1, 2, 3, 7, 8, 9, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()
