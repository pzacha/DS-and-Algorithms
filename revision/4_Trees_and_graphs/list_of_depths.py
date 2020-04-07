import unittest

from binary_search_tree import Node
from minimal_tree import minimal_tree


class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self, n=None):
        self.head = n

    def add(self, d):
        n = LLNode(d)
        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def __len__(self):
        l = 0
        n = self.head
        while n:
            l += 1
            n = n.next

        return l


def list_of_depths(n, depth, output):
    if n:
        depth += 1
        while len(output) < depth:
            output.append(SLinkedList())

        if n.left:
            list_of_depths(n.left, depth, output)

        output[depth - 1].add(LLNode(n))

        if n.right:
            list_of_depths(n.right, depth, output)
        depth -= 1


class Test(unittest.TestCase):
    arr = [1, 4, 5, 6, 9, 11, 14, 15, 15, 21, 23]
    bst = Node()
    minimal_tree(arr, bst)
    output = []
    list_of_depths(bst, 0, output)

    def test_list_of_depths(self):
        self.assertEqual(len(self.output[2]), 4)


if __name__ == "__main__":
    unittest.main()
