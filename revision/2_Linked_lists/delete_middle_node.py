import unittest


def delete_middle(node):
    node.data = node.next.data
    node.next = node.next.next
