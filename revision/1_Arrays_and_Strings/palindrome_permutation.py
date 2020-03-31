import unittest


def palindrome_permutation(s: str) -> bool:
    char_dict = {}
    uneven = 0
    for c in s:
        if c != " ":
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    for k in char_dict:
        if char_dict[k] % 2 == 1:
            uneven += 1
        if uneven > 1:
            return False
    return True


class Test(unittest.TestCase):
    dataT = [("abcd c a bed"), ("doggydogg")]
    dataF = [("america"), ("cook")]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            self.assertTrue(palindrome_permutation(test_string))
        # false check
        for test_string in self.dataF:
            self.assertFalse(palindrome_permutation(test_string))


if __name__ == "__main__":
    unittest.main()
