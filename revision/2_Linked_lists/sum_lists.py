import unittest
from linked_list import SLinkedList, Node


def sum_lists(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    s1 = ""
    s2 = ""
    while n1:
        s1 += str(n1.data)
        n1 = n1.next
    while n2:
        s2 += str(n2.data)
        n2 = n2.next
    sum = str(int(s1) + int(s2))
    output = SLinkedList()
    for d in sum:
        output.insert_at_end(int(d))
    return output


class Test(unittest.TestCase):
    lin_list1 = SLinkedList()
    lin_list1.insert_vals_at_end([2, 7, 2])
    lin_list2 = SLinkedList()
    lin_list2.insert_vals_at_end([1, 1, 2])

    def test_sum_lists(self):
        calculated = sum_lists(self.lin_list1, self.lin_list2)
        calculated = calculated.to_list()
        self.assertEqual(calculated, [3, 8, 4])


if __name__ == "__main__":
    unittest.main()
