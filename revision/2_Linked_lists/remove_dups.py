import unittest

from linked_list import SLinkedList, Node


def remove_dups(LList):
    values = []
    n = LList.head
    while n.next != None:
        if n.next.data in values:
            n.next = n.next.next
        else:
            values.append(n.next.data)
        n = n.next
    return LList


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.head = Node(5)
    lin_list.head.next = Node(2)
    lin_list.insert_at_end(7)
    lin_list.insert_at_end(2)
    lin_list.insert_at_end(3)
    expected = [5, 2, 7, 3]

    def test_remove_dups(self):
        calculated = remove_dups(self.lin_list)
        calculated = calculated.to_list()
        self.assertEqual(self.expected, calculated)


if __name__ == "__main__":
    unittest.main()
