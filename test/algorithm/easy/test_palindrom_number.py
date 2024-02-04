import unittest

from src.algorithm.easy.palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    def test_case_one(self):
        x = 121
        res = Solution().isPalindrome(x)
        assert res == True


if __name__ == '__main__':
    unittest.main()
