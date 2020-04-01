import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substring(2 * s1, s2)


class Test(unittest.TestCase):
    dataT = [("waterbottle", "erbottlewat"), ("paleman", "npalema")]
    dataF = [("waterbottle", "erbotttlewa"), ("paleman", "npaleman")]

    def test_unique(self):
        # true check
        for test_strings in self.dataT:
            self.assertTrue(string_rotation(test_strings[0], test_strings[1]))
        # false check
        for test_strings in self.dataF:
            self.assertFalse(string_rotation(test_strings[0], test_strings[1]))


if __name__ == "__main__":
    unittest.main()
