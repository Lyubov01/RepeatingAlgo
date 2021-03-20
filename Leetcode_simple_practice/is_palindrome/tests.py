import unittest
from isPalindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(is_palindrome(121), True)

    def testcase2(self):
        self.assertEqual(is_palindrome(23), False)

    def testcase3(self):
        self.assertEqual(is_palindrome(178871), True)

    def testcase4(self):
        self.assertEqual(is_palindrome(-101), False)

    def testcase5(self):
        self.assertEqual(is_palindrome(10), False)

    def testcase6(self):
        self.assertEqual(is_palindrome(1), True)

    def testcase7(self):
        self.assertEqual(is_palindrome(10000), False)


if __name__ == '__main__':
    unittest.main()
