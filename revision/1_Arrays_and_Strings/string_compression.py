import unittest


def string_compression(s: str) -> str:
    output = ""
    count = 1
    for i in range(len(s)):
        if i == 0:
            output += s[i]
        else:
            if s[i] != s[i - 1]:
                output += str(count)
                count = 1
                output += s[i]
            else:
                count += 1
    output += str(count)

    if len(output) < len(s):
        return output
    else:
        return s


print(string_compression("aaaaaaaassdcfeecdd"))
print(string_compression("aaassdcfeecdd"))


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aaaaaaaassdcfeecdd", "a8s2d1c1f1e2c1d2"),
        ("aaassdcfeecdd", "aaassdcfeecdd"),
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
