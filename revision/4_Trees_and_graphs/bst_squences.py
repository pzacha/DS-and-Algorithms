import unittest

from binary_search_tree import Node
from minimal_tree import minimal_tree


def weave(first, second):
    result = []

    def rec_weave(first, second, prefix, result):
        if len(first) > 0:
            rec_weave(first[1:], second, prefix + [first[0]], result)

        if len(second) > 0:
            rec_weave(first, second[1:], prefix + [second[0]], result)

        if len(first) == 0 and len(second) == 0:
            result.append(prefix)

    rec_weave(first, second, [], result)
    return result


def multi_weave(output_left, output_right):
    output = []
    for l in output_left:
        for r in output_right:
            for w in weave(l, r):
                output.append(w)
    return output


def bst_sequences(n):
    output = []

    def rec_sequences(n):
        output = []
        if n:
            if n.left:
                output_left = rec_sequences(n.left)
                output = output_left
            if n.right:
                output_right = rec_sequences(n.right)
                output = output_right

            if n.left == None and n.right == None:
                output.append([n.data])
            elif n.left != None and n.right != None:
                output = multi_weave(output_left, output_right)
                for l in output:
                    l.insert(0, n.data)
            else:
                for l in output:
                    l.insert(0, n.data)
        return output

    output = rec_sequences(n)
    return output


class Test(unittest.TestCase):
    arr = [1, 2, 3]
    bst = Node()
    minimal_tree(arr, bst)
    output = bst_sequences(bst)

    def test_minimal_tree(self):
        self.assertEqual(self.output, [[2, 1, 3], [2, 3, 1]])


if __name__ == "__main__":
    unittest.main()
