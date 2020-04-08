import unittest

from binary_search_tree import Node
from minimal_tree import minimal_tree


def check_balanced(n):
    h_left = 0
    h_right = 0
    if n:
        # Check if heights of left and right nodes are the same
        if n.left:
            h_left = calc_node_height(n.left)
        if n.right:
            h_right = calc_node_height(n.right)
        if abs(h_left - h_right) > 1:
            return False
        # Repeat for subtrees
        if n.left:
            check_balanced(n.left)
        if n.right:
            check_balanced(n.right)
    return True


def calc_node_height(n):
    h = 0
    max_height = 0

    def calc_height(n, height, max_height):
        if n:
            height += 1
            if n.left:
                max_height = calc_height(n.left, height, max_height)
            if n.right:
                max_height = calc_height(n.right, height, max_height)
            if height > max_height:
                max_height = height
            height -= 1

        return max_height

    max_height = calc_height(n, h, max_height)

    return max_height


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = Node()
    minimal_tree(arr, bst)
    unbal = Node(6)

    def test_check_balanced(self):
        self.assertEqual(True, check_balanced(self.bst))
        [self.unbal.insert(i) for i in range(2, 19, 3)]
        self.assertEqual(False, check_balanced(self.unbal))


if __name__ == "__main__":
    unittest.main()
