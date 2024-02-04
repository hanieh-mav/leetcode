import unittest

from src.algorithm.easy.roman_to_integer import Solution


class TestRomanToInteger(unittest.TestCase):

    def test_case_one(self):
        s = 'III'
        res = Solution().romanToInt(s)
        assert res == 3

    def test_case_two(self):
        s = 'LVIII'
        res = Solution().romanToInt(s)
        assert res == 58

    def test_case_three(self):
        s = 'MCMXCIV'
        res = Solution().romanToInt(s)
        assert res == 1994
