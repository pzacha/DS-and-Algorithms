import unittest

from binary_search_tree import Node


def minimal_tree(arr):
    l = len(arr)
    mid = l / 2
    if l % 2 == 1:
        mid -= 0.5

    bst = Node(arr[int(mid)])

    for i in range(l):
        if i != mid:
            bst.insert(arr[i])

    return bst


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = minimal_tree(arr)
    output = []
    bst.in_order_traversal(output)

    def test_minimal_tree(self):
        self.assertEqual(self.output, self.arr)


if __name__ == "__main__":
    unittest.main()
