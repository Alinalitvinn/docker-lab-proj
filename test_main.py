import unittest
from main import StringUtils

class TestStringUtils(unittest.TestCase):
    def test_string_length(self):
        self.assertEqual(StringUtils.string_length("hello"), 5)
        self.assertEqual(StringUtils.string_length(""), 0)
        self.assertEqual(StringUtils.string_length("123456789"), 9)

    def test_reverse_string(self):
        self.assertEqual(StringUtils.reverse_string("hello"), "olleh")
        self.assertEqual(StringUtils.reverse_string(""), "")
        self.assertEqual(StringUtils.reverse_string("12345"), "54321")

    def test_uppercase_string(self):
        self.assertEqual(StringUtils.uppercase_string("hello"), "HELLO")
        self.assertEqual(StringUtils.uppercase_string(""), "")
        self.assertEqual(StringUtils.uppercase_string("AbCdEfG"), "ABCDEFG")

if __name__ == '__main__':
    unittest.main()
