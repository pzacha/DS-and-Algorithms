import unittest


def rotate_matrix(m):
    l = len(m)
    for i in range(l // 2):
        first, last = i, l - i - 1
        for j in range(first, last):
            temp = m[i][j]
            m[i][j] = m[-j - 1][i]
            m[-j - 1][i] = m[-i - 1][-j - 1]
            m[-i - 1][-j - 1] = m[j][-i - 1]
            m[j][-i - 1] = temp
    return m


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        )
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
