import unittest

from binary_search_tree import Node


def paths_with_sum(n: Node, s: int):
    searched_sum = s
    output = 0

    def find_sum(n: Node, vals: list, output: int):
        vals.append(n.data)
        for i in range(len(vals)):
            if sum(vals[i:]) == searched_sum:
                output += 1
        if n.left:
            output = find_sum(n.left, vals, output)
        if n.right:
            output = find_sum(n.right, vals, output)
        vals.pop()
        return output

    output = find_sum(n, [], output)
    return output


class Test(unittest.TestCase):
    root = Node(1)
    root.right = Node(3)
    root.left = Node(5)
    root.left.right = Node(-4)
    root.left.right.right = Node(3)
    root.left.left = Node(-2)
    root.left.left.right = Node(10)
    root.left.left.left = Node(4)

    def test_paths_with_sum(self):
        self.assertEqual(paths_with_sum(self.root, 4), 4)


if __name__ == "__main__":
    unittest.main()
