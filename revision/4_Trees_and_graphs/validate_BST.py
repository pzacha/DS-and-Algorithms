import unittest

from binary_search_tree import Node
from minimal_tree import minimal_tree


def val_bst(n):
    output = []

    def val_bst_rec(n, output):
        if n:
            if n.left:
                val_bst_rec(n.left, output)
            output.append(n.data)
            if n.right:
                val_bst_rec(n.right, output)

    val_bst_rec(n, output)
    return output


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = Node()
    minimal_tree(arr, bst)
    output = val_bst(bst)

    def test_validate_bst(self):
        self.assertEqual([1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23], self.output)


if __name__ == "__main__":
    unittest.main()
