import unittest
from linked_list import SLinkedList, Node


def intersection(ll1, ll2):
    l1 = len(ll1)
    l2 = len(ll2)
    n1 = ll1.head
    n2 = ll2.head
    if l1 > l2:
        for i in range(l1 - l2):
            n1 = n1.next
    elif l2 < l1:
        for i in range(l2 - l1):
            n2 = n2.next
    while n1 or n2:
        if n1 == n2:
            return True
        n1 = n1.next
        n2 = n2.next
    return False


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.insert_vals_at_end([2, 7, 2])
    lin_list2 = SLinkedList()
    lin_list2.head = Node(5)
    lin_list2.head.next = lin_list.head.next.next

    def test_intersection(self):
        self.assertEqual(intersection(self.lin_list, self.lin_list2), True)


if __name__ == "__main__":
    unittest.main()
