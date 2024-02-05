import unittest

from src.algorithm.easy.valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test_case_one(self):
        s = "()"
        res = Solution().isValid(s)
        assert res is True

    def test_case_two(self):
        s = "()[]{}"
        res = Solution().isValid(s)
        assert res is True

    def test_case_three(self):
        s = "(]"
        res = Solution().isValid(s)
        assert res is False


if __name__ == '__main__':
    unittest.main()
