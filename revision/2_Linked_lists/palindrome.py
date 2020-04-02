import unittest
from linked_list import SLinkedList, Node


def palindrome(ll):
    reversed_ll = SLinkedList()
    n = ll.head
    while n:
        reversed_ll.insert_at_beginning(n.data)
        n = n.next
    n1 = ll.head
    n2 = reversed_ll.head
    while n1 and n2:
        if n1.data != n2.data:
            return False
        n1 = n1.next
        n2 = n2.next
    return True


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.insert_vals_at_end([2, 7, 2])
    lin_list2 = SLinkedList()
    lin_list2.insert_vals_at_end([2, 7, 7, 2])
    lin_list3 = SLinkedList()
    lin_list3.insert_vals_at_end([2, 1, 7, 2])

    def test_palindrome(self):
        self.assertEqual(palindrome(self.lin_list), True)
        self.assertEqual(palindrome(self.lin_list2), True)
        self.assertEqual(palindrome(self.lin_list3), False)


if __name__ == "__main__":
    unittest.main()
