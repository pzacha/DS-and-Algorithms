import unittest

from linked_list import SLinkedList, Node


def kth_to_last(ll, k):
    if k > len(ll):
        return None
    l = len(ll) - k
    n = ll.head
    for i in range(l):
        n = n.next
    return n


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.head = Node(1)
    lin_list.head.next = Node(2)
    lin_list.insert_at_end(3)
    lin_list.insert_at_end(4)
    lin_list.insert_at_end(5)

    def test_kth_to_last(self):
        calculated = kth_to_last(self.lin_list, 2)
        self.assertEqual(calculated.data, 4)


if __name__ == "__main__":
    unittest.main()
