import unittest


def is_unique(s: str) -> bool:
    for i in range(0, len(s) - 1):
        if s[i] in s[i + 1 :]:
            return False

    return True


class Test(unittest.TestCase):
    dataT = [("abcd"), ("s4fad"), ("")]
    dataF = [("23ds2"), ("hb 627jh=j ()")]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            self.assertTrue(is_unique(test_string))
        # false check
        for test_string in self.dataF:
            self.assertFalse(is_unique(test_string))


if __name__ == "__main__":
    unittest.main()
