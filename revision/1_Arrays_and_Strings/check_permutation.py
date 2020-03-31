import unittest


def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    s2_dict = {}
    for c in s1:
        if c in s1_dict:
            s1_dict[c] += 1
        else:
            s1_dict[c] = 1

    for c in s2:
        if c in s2_dict:
            s2_dict[c] += 1
        else:
            s2_dict[c] = 1

    if s1_dict == s2_dict:
        return True
    else:
        return False


class Test(unittest.TestCase):
    dataT = [["abcded", "dabced"], ["adaa", "aaad"]]
    dataF = [["23ds2", "23ds3"], ["sscx", "asdasdasd"]]

    def test_unique(self):
        # true check
        for test_strings in self.dataT:
            self.assertTrue(check_permutation(test_strings[0], test_strings[1]))
        # false check
        for test_strings in self.dataF:
            self.assertFalse(check_permutation(test_strings[0], test_strings[1]))


if __name__ == "__main__":
    unittest.main()
