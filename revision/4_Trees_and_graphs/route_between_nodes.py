import unittest

from node_graph import Node, Graph


class Test(unittest.TestCase):
    test_data = Graph()
    test_data.add_node(Node())
    test_data.add_node(Node())
    test_data.add_node(Node())

    def test_route_between_nodes(self):
        self.assertEqual(self.o1, "Dog1")


if __name__ == "__main__":
    unittest.main()
