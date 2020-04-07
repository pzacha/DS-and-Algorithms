import unittest

from binary_search_tree import Node


def minimal_tree(arr, bst):
    l = len(arr)
    if l == 1:
        bst.insert(arr[0])
    elif l == 2:
        bst.insert(arr[0])
        bst.insert(arr[1])
    else:
        mid = l / 2
        if l % 2 == 1:
            mid -= 0.5
        mid = int(mid)
        bst.insert(arr[mid])
        minimal_tree(arr[:mid], bst)
        minimal_tree(arr[mid + 1 :], bst)


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = Node()
    minimal_tree(arr, bst)
    output = []
    bst.in_order_traversal(output)

    def test_minimal_tree(self):
        self.assertEqual(self.output, self.arr)


if __name__ == "__main__":
    unittest.main()
