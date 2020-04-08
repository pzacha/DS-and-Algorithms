import unittest

from binary_search_tree import Node
from minimal_tree import minimal_tree


def val_bst(n):
    previous = None

    def val_bst_rec(n, previous):
        if n:
            if n.left:
                val_bst_rec(n.left, previous)
            if previous == None or previous <= n.data:
                previous = n.data
            else:
                return False
            if n.right:
                val_bst_rec(n.right, previous)

    val_bst_rec(n, previous)
    return True


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = Node()
    minimal_tree(arr, bst)
    output = val_bst(bst)

    def test_validate_bst(self):
        self.assertEqual(True, self.output)


if __name__ == "__main__":
    unittest.main()
