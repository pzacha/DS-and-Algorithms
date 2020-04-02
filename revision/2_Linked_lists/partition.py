import unittest
from linked_list import SLinkedList, Node


def partition(ll, x):
    n = ll.head
    less = SLinkedList()
    greater = SLinkedList()
    while n:
        next = n.next
        n.next = None
        if n.data < x:
            if less.head is None:
                less.head = n
            else:
                less.insert_at_beginning(n.data)
        else:
            if greater.head is None:
                greater.head = n
            else:
                greater.insert_at_beginning(n.data)
        n = next
    # Merging
    last_node = less.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = greater.head
    return less


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.insert_vals_at_end([2, 7, 2, 5, 9, 4, 11, 3])

    def test_partition(self):
        calculated = partition(self.lin_list, 5)
        calculated = calculated.to_list()
        self.assertEqual(calculated, [3, 4, 2, 2, 11, 9, 5, 7])


if __name__ == "__main__":
    unittest.main()
