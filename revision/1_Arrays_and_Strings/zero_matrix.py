import unittest


def zero_matrix(m):
    l = len(m)
    i_0 = []
    j_0 = []
    for i in range(l):
        for j in range(l):
            if m[i][j] == 0:
                if i not in i_0:
                    i_0.append(i)
                if j not in j_0:
                    j_0.append(j)
    for i in i_0:
        m[i] = [0 for x in m[i]]
    for j in j_0:
        for x in range(l):
            m[x][j] = 0
    return m


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        (
            [
                [1, 2, 3, 4, 5],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 0],
            ],
            [
                [1, 0, 3, 4, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [16, 0, 18, 19, 0],
                [0, 0, 0, 0, 0],
            ],
        )
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
