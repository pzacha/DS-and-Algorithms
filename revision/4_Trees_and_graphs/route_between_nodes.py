import unittest

from node_graph import Node, Graph


class Test(unittest.TestCase):
    test_data = Graph()
    for i in range(10):
        test_data.add_node(Node())

    for i in range(1, len(test_data.nodes) - 1):
        test_data.add_edge(test_data.nodes[0], test_data.nodes[i])

    test_data.dfs(test_data.nodes[0])

    def test_route_between_nodes(self):
        self.assertEqual(self.test_data.nodes[-1].visited, False)


if __name__ == "__main__":
    unittest.main()
