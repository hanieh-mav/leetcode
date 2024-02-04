import unittest

from src.algorithm.easy.palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    def test_case_one(self):
        x = 121
        res = Solution.isPalindrome(x)
        assert res == True

    def test_case_two(self):
        x = -121
        res = Solution.isPalindrome(x)
        assert res is False

    def test_case_three(self):
        x = 10
        res = Solution.isPalindrome(x)
        assert res is False


if __name__ == '__main__':
    unittest.main()
