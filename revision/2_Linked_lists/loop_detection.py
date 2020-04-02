import unittest
from linked_list import SLinkedList, Node


def loop_detection(ll):
    nodes = []
    n = ll.head
    while n:
        if n in nodes:
            return n
        else:
            nodes.append(n)
        n = n.next
    return None


class Test(unittest.TestCase):
    lin_list = SLinkedList()
    lin_list.head = Node(3)
    lin_list.head.next = Node(7)
    lin_list.head.next.next = Node(5)
    lin_list.head.next.next.next = lin_list.head.next

    lin_list2 = SLinkedList()
    lin_list2.head = Node(3)
    lin_list2.head.next = Node(7)
    lin_list2.head.next.next = Node(5)
    lin_list2.head.next.next.next = Node(11)

    def test_loop_detection(self):
        self.assertEqual(loop_detection(self.lin_list).data, 7)
        self.assertEqual(loop_detection(self.lin_list2), None)


if __name__ == "__main__":
    unittest.main()
